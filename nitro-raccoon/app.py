import os
import re
from functools import wraps
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import create_catalog, create_ratings
from models.user import User
from models.rating import Rating
from models.catalog.catalog_item import CatalogItem
from repositories import catalog_repo
from repositories import rating_repo
from repositories import user_repo
import image_upload
import template_helpers

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY não foi definida no arquivo .env")

# Filtro `brl` e globais usados nos templates (spec_rows, type_plural, ...).
template_helpers.init_app(app)

# Fotos dos itens ficam em static/uploads/items. O limite do Flask é só uma
# trava de segurança; a regra de 5 MB por foto está em image_upload.py.
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
UPLOAD_DIR = Path(app.static_folder) / 'uploads' / 'items'


def init_db():
    # Roda também com `flask run` (o bloco __main__ só roda com `python app.py`).
    # A ordem importa: ratings tem chave estrangeira para items_catalog.
    create_catalog()
    create_ratings()
    user_repo.create_users()


init_db()

# nome@dominio.tld: sem espaços, sem pontos duplicados, TLD só com letras (2+).
_EMAIL_RE = re.compile(
    r'^[A-Za-z0-9]+([._%+-][A-Za-z0-9]+)*'      # parte local
    r'@'
    r'[A-Za-z0-9]+(-[A-Za-z0-9]+)*'             # primeiro rótulo do domínio
    r'(\.[A-Za-z0-9]+(-[A-Za-z0-9]+)*)*'        # subdomínios opcionais
    r'\.[A-Za-z]{2,}$'                          # .com, .com.br, .org...
)


def is_valid_email(email):
    # 150 = tamanho da coluna users.email
    return len(email) <= 150 and _EMAIL_RE.fullmatch(email) is not None


@app.context_processor
def inject_user():
    user = None
    if 'user_id' in session:
        user = user_repo.seek_by_id(session['user_id'])
    # Os templates usam `current_user`; `user` fica por compatibilidade.
    return {'user': user, 'current_user': user}


def login_required(function):
    @wraps(function)
    def verify(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('login'))
        return function(*args, **kwargs)
    return verify


def admin_required(function):
    @wraps(function)
    def verify(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('login'))

        user = user_repo.seek_by_id(session['user_id'])
        if user is None or not user.is_admin:
            return redirect(url_for('panel'))

        return function(*args, **kwargs)
    return verify


@app.route('/')
def index():
    active_items = catalog_repo.list_active()
    logged = session.get('user_id') is not None
    return render_template('landing.html', items=active_items, logged=logged)


@app.route('/register-item', methods=['GET', 'POST'])
@admin_required
def register_item():
    if request.method == 'GET':
        return render_template(
            'register_item.html',
            sent=request.args.get('sent') == '1',
            form={},
        )

    form = request.form

    image = None

    def fail(message):
        # Se a foto já foi gravada mas o cadastro falhou, não deixa arquivo órfão.
        image_upload.delete_item_image(image, UPLOAD_DIR)
        return render_template('register_item.html', sent=False, form=form, error=message)

    item_type = form.get('item_type', '')
    if item_type not in CatalogItem.ITEM_TYPES:
        return fail('Escolha uma categoria.')

    try:
        image = image_upload.save_item_image(request.files.get('image'), UPLOAD_DIR)
    except ValueError as error:
        return fail(str(error))

    # Só os campos de especificação conhecidos entram; o formulário já envia
    # apenas os da categoria escolhida.
    # Campos em branco ficam de fora (NULL no banco) e Sim/Não viram 1/0,
    # porque '' em coluna INT e 'Sim' em coluna BOOLEAN dão erro no MySQL.
    bool_fields = {'non_slip_base', 'requires_power_supply'}
    specs = {}
    for key, value in form.items():
        value = value.strip()
        if key not in CatalogItem.SPEC_FIELDS or value == '':
            continue
        specs[key] = (1 if value == 'Sim' else 0) if key in bool_fields else value

    try:
        item = CatalogItem(
            form['code'].strip(),
            form['name'].strip(),
            item_type,
            form['price'],
            form.get('description', '').strip(),
            form['brand'].strip(),
            stock='pendente',  # todo item novo espera aprovação, não importa o que o POST diga
            **specs,
        )
        item.image = image
        catalog_repo.save(item)
    except ValueError as error:
        return fail(str(error))
    except mysql.connector.errors.IntegrityError:
        return fail('Já existe um item cadastrado com este código.')
    except mysql.connector.errors.DataError:
        return fail('Algum campo tem um valor grande demais ou em formato inválido. '
                    'Confira os dados e tente de novo.')

    # Redireciona para que atualizar a página não reenvie o cadastro.
    return redirect(url_for('register_item', sent=1))


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['senha']

        def fail(message):
            return render_template('sign_in.html', error=message, name=name, email=email)

        if not name:
            return fail('Informe seu nome.')
        if not is_valid_email(email):
            return fail('Informe um e-mail válido, como nome@exemplo.com.')
        if not password:
            return fail('Informe uma senha.')

        if user_repo.seek_by_email(email) is not None:
            return fail('Este e-mail já está cadastrado.')

        user = User(name, email, generate_password_hash(password))
        user_repo.save(user)
        return redirect(url_for('login'))

    return render_template('sign_in.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = user_repo.seek_by_email(email)
        if user and check_password_hash(user._hash_password, password):
            session['user_id'] = user.id
            return redirect(url_for('panel'))

        return render_template('login.html', error='E-mail ou senha inválidos.')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/panel')
@login_required
def panel():
    return render_template('panel.html', items=catalog_repo.list_active())


@app.route('/catalog')
@login_required
def catalog():
    # Itens pendentes só aparecem para administradores, em /admin.
    return render_template('catalog.html', catalog=catalog_repo.list_active())


@app.route('/catalog/<int:item_id>/rate', methods=['GET', 'POST'])
@login_required
def rate_item(item_id):
    item = catalog_repo.seek_by_items_id(item_id)
    if item is None:
        return redirect(url_for('catalog'))

    if request.method == 'POST':
        try:
            rating = Rating(request.form['costumer'], request.form['nota'])
        except ValueError as error:
            return render_template('rate.html', item=item, error=str(error))

        rating_repo.save(item_id, rating)
        return redirect(url_for('list_ratings', item_id=item_id))

    return render_template('rate.html', item=item)


@app.route('/item/<int:item_id>/ratings')
@login_required
def list_ratings(item_id):
    item = catalog_repo.list_complete(item_id)
    if item is None:
        return redirect(url_for('panel'))

    return render_template('ratings.html', item=item)


@app.route('/catalog/<int:item_id>/catalog')
@login_required
def list_catalog(item_id):
    item = catalog_repo.seek_by_items_id(item_id)
    if item is None:
        return redirect(url_for('catalog'))

    # Outros itens da mesma categoria.
    items = catalog_repo.list_by_category(item.item_type)
    return render_template('catalog.html', catalog=items, only_type=item.item_type)


@app.route('/admin')
@admin_required
def pendent_admin():
    pendent = catalog_repo.list_by_stock('pendente')
    return render_template('admin.html', catalog=pendent)


@app.route('/admin/catalog')
@admin_required
def item_admin():
    return render_template(
        'item_admin.html',
        items=catalog_repo.list_all(),
        stock_valid=CatalogItem.STATUS_VALIDO,
    )


@app.route('/admin/item/<int:item_id>/stock', methods=['POST'])
@admin_required
def admin_update_stock(item_id):
    new_stock = request.form['stock']

    if new_stock not in CatalogItem.STATUS_VALIDO:
        return redirect(url_for('item_admin'))

    catalog_repo.update_stock(item_id, new_stock)

    origin = request.form.get('origin', 'item_admin')
    if origin not in ('item_admin', 'pendent_admin'):
        origin = 'item_admin'
    return redirect(url_for(origin))


@app.route('/admin/item/<int:item_id>/image', methods=['POST'])
@admin_required
def admin_update_image(item_id):
    item = catalog_repo.seek_by_items_id(item_id)
    if item is None:
        return redirect(url_for('item_admin'))

    try:
        new_image = image_upload.save_item_image(request.files.get('image'), UPLOAD_DIR)
    except ValueError as error:
        flash(f'{item.name}: {error}')
        return redirect(url_for('item_admin'))

    if new_image:
        catalog_repo.update_image(item_id, new_image)
        image_upload.delete_item_image(item.image, UPLOAD_DIR)  # troca: apaga a foto antiga
    return redirect(url_for('item_admin'))

@app.route('/admin/users')
@admin_required
def user_admin():
    return render_template('user_admin.html', users=user_repo.list_all())


@app.route('/admin/user/<int:user_id>/admin', methods=['POST'])
@admin_required
def admin_toggle_admin(user_id):
    # Impede o admin de se rebaixar, o que garante que sempre sobra pelo menos um.
    if user_id == session['user_id']:
        flash('Você não pode alterar o seu próprio acesso.')
    else:
        user_repo.set_admin(user_id, request.form.get('is_admin') == '1')
    return redirect(url_for('user_admin'))


@app.route('/catalog/<int:item_id>/item_catalog/new_item')
@login_required
def new_catalog_item(item_id):
    # O cadastro de itens agora é feito em /register-item.
    return redirect(url_for('register_item'))


if __name__ == '__main__':
    app.run(debug=True)