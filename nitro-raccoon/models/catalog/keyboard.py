from models.catalog.catalog_item import CatalogItem

class Keyboard(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, keyboard_type, item_connection, layout, switch, key_count, lighting):
        super().__init__(code, name, price, description, brand, stock)
        self._keyboard_type = keyboard_type
        self._item_connection = item_connection
        self._layout = layout
        self._switch = switch
        self._key_count = key_count
        self._lighting = lighting