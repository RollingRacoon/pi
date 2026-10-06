from models.catalog.catalog_item import CatalogItem

class Microphone(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, microphone_type, polar_pattern, item_connection, frequency, sensitivity, sampling_rate):
        super().__init__(code, name, price, description, brand, stock)
        self._microphone_type = microphone_type
        self._polar_pattern = polar_pattern
        self._item_connection = item_connection
        self._frequency = frequency
        self._sensitivity = sensitivity
        self._sampling_rate = sampling_rate