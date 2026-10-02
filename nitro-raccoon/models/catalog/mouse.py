from models.catalog.catalog_item import CatalogItem

class Mouse(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, sensor, dpi, button_count, connection, polling_rate, weight):
        super().__init__(code, name, price, description, brand, stock)
        self._sensor = sensor
        self._dpi = dpi
        self._button_count = button_count
        self._connection = connection
        self._polling_rate = polling_rate
        self._weight = weight