from database.db import connect
from models.catalog.catalog_item import CatalogItem
from repositories import rating_repo

BASE_COLUMNS = ('code', 'name', 'price', 'item_type', 'description', 'brand', 'stock')

# Nomes de coluna vêm sempre de listas fixas (nunca do formulário), e os valores
# vão por parâmetros %s: o SQL montado aqui não aceita injeção.
_SELECT = (
    'SELECT items_id, '
    + ', '.join(f'`{column}`' for column in BASE_COLUMNS + CatalogItem.SPEC_FIELDS)
    + ', `image` FROM items_catalog'
)
_ACTIVE = ', '.join(['%s'] * len(CatalogItem.STATUS_ATIVOS))


def save(item):
    invalid = [field for field in item.specs if field not in CatalogItem.SPEC_FIELDS]
    if invalid:
        raise ValueError(f'Campos desconhecidos: {", ".join(invalid)}')

    columns = list(BASE_COLUMNS) + list(item.specs)
    values = [
        item.code, item.name, item.price, item.item_type,
        item.description, item.brand, item.stock,
    ] + list(item.specs.values())

    image = getattr(item, 'image', None)
    if image:
        columns.append('image')
        values.append(image)

    names = ', '.join(f'`{column}`' for column in columns)
    marks = ', '.join(['%s'] * len(columns))

    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(f'INSERT INTO items_catalog ({names}) VALUES ({marks})', values)
        connection.commit()
        item.id = cursor.lastrowid
    finally:
        connection.close()
    return item.id


def _row_to_item(row):
    items_id, code, name, price, item_type, description, brand, stock, *spec_values, image = row
    specs = {
        column: value
        for column, value in zip(CatalogItem.SPEC_FIELDS, spec_values)
        if value is not None
    }
    # Linhas antigas (stock numérico ou vazio) voltam como pendentes.
    if stock not in CatalogItem.STATUS_VALIDO:
        stock = 'pendente'

    item = CatalogItem(code, name, item_type, price, description, brand, stock, **specs)
    item.id = items_id
    item.image = image
    return item


def _fetch(clause='', params=()):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(f'{_SELECT} {clause}', params)
        rows = cursor.fetchall()
    finally:
        connection.close()
    return [_row_to_item(row) for row in rows]


def seek_by_items_id(items_id):
    items = _fetch('WHERE items_id = %s', (items_id,))
    return items[0] if items else None


def list_all():
    return _fetch('ORDER BY item_type, name')


def list_active():
    return _fetch(
        f'WHERE stock IN ({_ACTIVE}) ORDER BY item_type, name',
        CatalogItem.STATUS_ATIVOS,
    )


def list_by_category(item_type):
    return _fetch(
        f'WHERE item_type = %s AND stock IN ({_ACTIVE}) ORDER BY name',
        (item_type, *CatalogItem.STATUS_ATIVOS),
    )


def list_by_stock(stock):
    return _fetch('WHERE stock = %s ORDER BY items_id', (stock,))


def update_stock(items_id, new_stock):
    if new_stock not in CatalogItem.STATUS_VALIDO:
        raise ValueError(f'Estoque inválido: {new_stock}')

    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE items_catalog SET stock = %s WHERE items_id = %s',
            (new_stock, items_id),
        )
        connection.commit()
    finally:
        connection.close()


def list_complete(items_id):
    item = seek_by_items_id(items_id)
    if item is None:
        return None
    item.ratings = rating_repo.list_score_by_item(items_id)
    return item

def update_image(items_id, image):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE items_catalog SET image = %s WHERE items_id = %s',
            (image, items_id),
        )
        connection.commit()
    finally:
        connection.close()