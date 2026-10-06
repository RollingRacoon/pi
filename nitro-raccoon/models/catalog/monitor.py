from models.catalog.catalog_item import CatalogItem

class Monitor(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, size, resolution, refresh_rate, response, display_type, proportion, item_connection):
        super().__init__(code, name, price, description, brand, stock)
        self._size = size
        self._resolution = resolution
        self._refresh_rate = refresh_rate
        self._response = response
        self._display_type = display_type
        self._proportion = proportion
        self._item_connection = item_connection