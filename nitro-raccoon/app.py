import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import create_catalog, create_ratings
from models.user import User
from models.rating import Rating
from models.catalog.catalog_item import CatalogItem
from models.catalog.adapter import Adapter
from models.catalog.air_cooler import AirCooler
from models.catalog.cable import Cable
from models.catalog.cpu import CPU
from models.catalog.fan import Fan
from models.catalog.gpu import GPU
from models.catalog.keyboard import Keyboard
from models.catalog.microphone import Microphone
from models.catalog.monitor import Monitor
from models.catalog.mother_board import MotherBoard
from models.catalog.mouse import Mouse
from models.catalog.mouse_pad import MousePad
from models.catalog.pc_case import PCCase
from models.catalog.psu import PSU
from models.catalog.ram import RAM
from models.catalog.storage import Storage
from models.catalog.water_cooler import WaterCooler
from repositories import catalog_repo
from repositories import rating_repo
from repositories import user_repo

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY não foi definida no arquivo .env")

@app.context_processor
def inject_current_user():
    current_user = None
    if 'user_id' in session:
        current_user = user_repo.seek_by_id(session['user_id'])
    return {'current_user': current_user}

def login_required(function):
    @wraps(function)
    def verify(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return function(*args, **kwargs)
    return verify

def admin_required(function):
    @wraps(function)
    def verify(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user = user_repo.seek_by_id(session['user_id'])
        if user is None or not user.is_admin:
            return redirect(url_for('panel'))

        return function(*args, **kwargs)
    return verify

@app.route('/')
def index():
    active_items = catalog_repo.list_by_stock('active')
    logged = 'user_id' in session
    return render_template('landing.html', items=active_items, logged=logged)

@app.route('/register-item', methods=['GET', 'POST'])
def register_item():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        item_type = request.form['item_type']
        price = request.form['price']
        description = request.form['description']
        brand = request.form['brand']
        stock = request.form['stock']
        adapter_type = request.form.get('adapter_type')
        air_cooler_type = request.form.get('air_cooler_type')
        cable_type = request.form.get('cable_type')
        keyboard_type = request.form.get('keyboard_type')
        microphone_type = request.form.get('microphone_type')
        mouse_pad_type = request.form.get('mouse_pad_type')
        psu_type = request.form.get('psu_type')
        ram_type = request.form.get('ram_type')
        storage_type = request.form.get('storage_type')
        water_cooler_type = request.form.get('water_cooler_type')
        item_connection = request.form.get('item_connection')
        socket = request.form.get('socket')
        socket_compatibility = request.form.get('socket_compatibility')
        chipset = request.form.get('chipset')
        interface = request.form.get('interface')
        form_factor = request.form.get('form_factor')
        pc_case_format = request.form.get('pc_case_format')
        storage_format = request.form.get('storage_format')
        size = request.form.get('size')
        lighting = request.form.get('lighting')
        material = request.form.get('material')
        length = request.form.get('length')
        width = request.form.get('width')
        thickness = request.form.get('thickness')
        voltage = request.form.get('voltage')
        capacity = request.form.get('capacity')
        frequency = request.form.get('frequency')
        input_connector = request.form.get('input_connector')
        output_connector = request.form.get('output_connector')
        source_interface = request.form.get('source_interface')
        target_interface = request.form.get('target_interface')
        compatibility = request.form.get('compatibility')
        version = request.form.get('version')
        transfer_speed = request.form.get('transfer_speed')
        max_power = request.form.get('max_power')
        max_resolution = request.form.get('max_resolution')
        requires_power_supply = request.form.get('requires_power_supply')
        supported_tdp = request.form.get('supported_tdp')
        fan_rotation = request.form.get('fan_rotation')
        fan_number = request.form.get('fan_number')
        radiator_size = request.form.get('radiator_size')
        cores = request.form.get('cores')
        threads = request.form.get('threads')
        base_frequency = request.form.get('base_frequency')
        turbo_frequency = request.form.get('turbo_frequency')
        cache = request.form.get('cache')
        tdp = request.form.get('tdp')
        max_rpm = request.form.get('max_rpm')
        cfm = request.form.get('cfm')
        static_pressure = request.form.get('static_pressure')
        bearing_type = request.form.get('bearing_type')
        connector_type = request.form.get('connector_type')
        noise_level = request.form.get('noise_level')
        led_number = request.form.get('led_number')
        vram = request.form.get('vram')
        memory_type = request.form.get('memory_type')
        clock = request.form.get('clock')
        consumption = request.form.get('consumption')
        layout = request.form.get('layout')
        switch = request.form.get('switch')
        key_count = request.form.get('key_count')
        polar_pattern = request.form.get('polar_pattern')
        sensitivity = request.form.get('sensitivity')
        sampling_rate = request.form.get('sampling_rate')
        resolution = request.form.get('resolution')
        refresh_rate = request.form.get('refresh_rate')
        response = request.form.get('response')
        display_type = request.form.get('display_type')
        proportion = request.form.get('proportion')
        ram_slots = request.form.get('ram_slots')
        ram_capacity = request.form.get('ram_capacity')
        m2_slots = request.form.get('m2_slots')
        pcie_slots = request.form.get('pcie_slots')
        sensor = request.form.get('sensor')
        dpi = request.form.get('dpi')
        button_count = request.form.get('button_count')
        polling_rate = request.form.get('polling_rate')
        weight = request.form.get('weight')
        non_slip_base = request.form.get('non_slip_base')
        max_gpu_length = request.form.get('max_gpu_length')
        max_cooler_height = request.form.get('max_cooler_height')
        supported_radiator = request.form.get('supported_radiator')
        panel_type = request.form.get('panel_type')
        potency = request.form.get('potency')
        certification = request.form.get('certification')
        modularity = request.form.get('modularity')
        fan = request.form.get('fan')
        connectors = request.form.get('connectors')
        modules = request.form.get('modules')
        latency = request.form.get('latency')
        reading_speed = request.form.get('reading_speed')
        writing_speed = request.form.get('writing_speed')

        new_item = CatalogItem(code, name, item_type, price, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
        catalog_repo.save(new_item)
        return render_template('register_item.html', sent=True)

    return render_template('register_item.html', sent=False)

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hash_password = generate_password_hash(request.form['senha'])

        if user_repo.seek_by_email(email) is not None:
            return render_template('sign_in.html', error='Este e-mail já está cadastrado.')

        user = User(name, email, hash_password)
        user_repo.save(user)
        return redirect(url_for(login))

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
    user = user_repo.seek_by_id(session['user_id'])
    return render_template('panel.html', user=user)

@app.route('/catalog')
@login_required
def catalog():
    list_catalog = catalog_repo.list_all()
    return render_template('catalog.html', catalog=list_catalog)

@app.route('/catalog/<int:item_id>/rate', methods=['GET', 'POST'])
@login_required
def rate_item(item_id):
    item = catalog_repo.seek_by_items_id(item_id)
    if item is None:
        return redirect(url_for('catalog'))

    if request.method == 'POST':
        costumer = request.form['costumer']
        score = float(request.form['nota'])

        rating = Rating(costumer, score)
        rating_repo.save(item_id, rating)
        return redirect(url_for('list_ratings', item_id=item_id))

    return render_template('rate.html', item=item)

@app.route('/item/<int:item_id>/ratings')
@login_required
def list_ratings(item_id):
    item = catalog_repo.list_complete(item_id)
    if item is None:
        return redirect(url_for('items_catalog'))

    return render_template('ratings.html', item=item)

@app.route('/catalog/<int:item_id>/catalog')
@login_required
def list_catalog(item_id):
    catalog = catalog_repo.seek_by_items_id(item_id)
    if catalog is None:

        items = catalog_repo.list_by_category(item_id)

        adapter = [item for item in items if isinstance(item, Adapter)]
        air_cooler = [item for item in items if isinstance(item, AirCooler)]
        cable = [item for item in items if isinstance(item, Cable)]
        cpu = [item for item in items if isinstance(item, CPU)]
        fan = [item for item in items if isinstance(item, Fan)]
        gpu = [item for item in items if isinstance(item, GPU)]
        keyboard = [item for item in items if isinstance(item, Keyboard)]
        microphone = [item for item in items if isinstance(item, Microphone)]
        monitor = [item for item in items if isinstance(item, Monitor)]
        mother_board = [item for item in items if isinstance(item, MotherBoard)]
        mouse_pad = [item for item in items if isinstance(item, MousePad)]
        mouse = [item for item in items if isinstance(item, Mouse)]
        pc_case = [item for item in items if isinstance(item, PCCase)]
        psu = [item for item in items if isinstance(item, PSU)]
        ram = [item for item in items if isinstance(item, RAM)]
        storage = [item for item in items if isinstance(item, Storage)]
        water_cooler = [item for item in items if isinstance(item, WaterCooler)]

        return render_template(
            'catalog.html', 
            adapter=adapter,
            air_cooler=air_cooler,
            cable=cable,
            cpu=cpu,
            fan=fan,
            gpu=gpu,
            keyboard=keyboard,
            microphone=microphone,
            monitor=monitor,
            mother_board=mother_board,
            mouse_pad=mouse_pad,
            mouse=mouse,
            pc_case=pc_case,
            psu=psu,
            ram=ram,
            storage=storage,
            water_cooler=water_cooler
        )

@app.route('/admin')
@admin_required
def pendent_admin():
    pendent = catalog_repo.list_by_stock('pendente')
    return render_template('admin.html', catalog=pendent)

@app.route('/admin/catalog')
@admin_required
def item_admin():
    all = catalog_repo.list_all()
    return render_template(
        'item_admin.html',
        items=all,
        stock_valid=CatalogItem.STATUS_VALIDO
    )

@app.route('/admin/item/<int:item_id>/stock', methods=['POST'])
@admin_required
def admin_update_stock(item_id):
    new_stock = request.form['stock']

    if new_stock not in CatalogItem.STATUS_VALIDO:
        return redirect(url_for('item_admin'))

    catalog_repo.update_stock(item_id, new_stock)

    origin = request.form.get('origin', 'item_admin')
    return redirect(url_for(origin))

@app.route('/catalog/<int:item_id>/item_catalog/new_item')
@login_required
def new_catalog_item(item_id):
    item = catalog_repo.seek_by_items_id(item_id)
    if item is None:
        return redirect(url_for('catalog'))

    if request.method == 'POST':
        item_type = request.form['item_type']
        name = request.form['name']
        brand = request.form['brand']
        code = request.form['code']
        description = request.form['description']
        price = float(request.form['price'])

        if item_type == 'adapter':
            item = Adapter(name, price, description, brand, code, request.form.get('adapter_type', 'input_connector', 'output_connector', 'source_interface', 'target_interface', 'compatibility', 'version', 'transfer_speed', 'max_power', 'max_resolution', 'requires_power_supply'))
        elif item_type == 'air_cooler':
            item = AirCooler(name, price, description, brand, code, request.form.get('socket_compatibility'), request.form.get('fan_size'), request.form.get('height'), request.form.get('tdp'), request.form.get('noise_level'), request.form.get('rgb'))
        elif item_type == 'cable':
            item = Cable(name, price, description, brand, code, request.form.get('cable_type'), request.form.get('length'), request.form.get('connector_a'), request.form.get('connector_b'), request.form.get('max_speed'), request.form.get('shielded'))
        elif item_type == 'cpu':
            item = CPU(name, price, description, brand, code, request.form.get('socket'), request.form.get('cores'), request.form.get('threads'), request.form.get('base_clock'), request.form.get('boost_clock'), request.form.get('tdp'), request.form.get('integrated_graphics'))
        elif item_type == 'fan':
            item = Fan(name, price, description, brand, code, request.form.get('size'), request.form.get('rpm'), request.form.get('airflow'), request.form.get('noise_level'), request.form.get('connector'), request.form.get('rgb'))
        elif item_type == 'gpu':
            item = GPU(name, price, description, brand, code, request.form.get('chipset'), request.form.get('vram'), request.form.get('memory_type'), request.form.get('boost_clock'), request.form.get('tdp'), request.form.get('length'), request.form.get('interface'))
        elif item_type == 'keyboard':
            item = Keyboard(name, price, description, brand, code, request.form.get('layout'), request.form.get('switch_type'), request.form.get('connection'), request.form.get('backlight'), request.form.get('form_factor'))
        elif item_type == 'microphone':
            item = Microphone(name, price, description, brand, code, request.form.get('mic_type'), request.form.get('polar_pattern'), request.form.get('connection'), request.form.get('frequency_response'), request.form.get('sample_rate'))
        elif item_type == 'monitor':
            item = Monitor(name, price, description, brand, code, request.form.get('screen_size'), request.form.get('resolution'), request.form.get('refresh_rate'), request.form.get('panel_type'), request.form.get('response_time'), request.form.get('ports'))
        elif item_type == 'mother_board':
            item = MotherBoard(name, price, description, brand, code, request.form.get('socket'), request.form.get('chipset'), request.form.get('form_factor'), request.form.get('ram_type'), request.form.get('ram_slots'), request.form.get('max_ram'), request.form.get('storage_interfaces'))
        elif item_type == 'mouse':
            item = Mouse(name, price, description, brand, code, request.form.get('dpi'), request.form.get('connection'), request.form.get('buttons'), request.form.get('sensor_type'), request.form.get('weight'), request.form.get('rgb'))
        elif item_type == 'mouse_pad':
            item = MousePad(name, price, description, brand, code, request.form.get('width'), request.form.get('height'), request.form.get('material'), request.form.get('surface_type'), request.form.get('rgb'))
        elif item_type == 'pc_case':
            item = PCCase(name, price, description, brand, code, request.form.get('form_factor'), request.form.get('supported_motherboards'), request.form.get('max_gpu_length'), request.form.get('max_cooler_height'), request.form.get('fan_slots'), request.form.get('side_panel'))
        elif item_type == 'psu':
            item = PSU(name, price, description, brand, code, request.form.get('wattage'), request.form.get('efficiency_rating'), request.form.get('modular'), request.form.get('form_factor'))
        elif item_type == 'ram':
            item = RAM(name, price, description, brand, code, request.form.get('capacity'), request.form.get('ram_type'), request.form.get('speed'), request.form.get('latency'), request.form.get('modules'))
        elif item_type == 'storage':
            item = Storage(name, price, description, brand, code, request.form.get('storage_type'), request.form.get('capacity'), request.form.get('interface'), request.form.get('read_speed'), request.form.get('write_speed'))
        elif item_type == 'water_cooler':
            item = WaterCooler(name, price, description, brand, code, request.form.get('radiator_size'), request.form.get('socket_compatibility'), request.form.get('tdp'), request.form.get('pump_speed'), request.form.get('noise_level'), request.form.get('rgb'))
        else:
            return render_template(
                'new_catalog_item.html', item=item, error='Tipe de item inválido.'
            )

        catalog_repo.save(item_id, item)
        return redirect(url_for('list_catalog', item_id=item_id))

    return render_template('new_catalog_item.html', item=item)


if __name__ == '__main__':
    create_catalog()
    create_ratings()
    user_repo.create_users()

    app.run(debug=True)