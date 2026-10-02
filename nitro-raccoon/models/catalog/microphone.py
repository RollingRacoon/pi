from models.catalog.catalog_item import CatalogItem

class Microphone(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, type, polar_pattern, connection, frequency, sensitivity, sampling_rate):
        super().__init__(code, name, price, description, brand, stock)
        self._type = type
        self._polar_pattern = polar_pattern
        self._connection = connection
        self._frequency = frequency
        self._sensitivity = sensitivity
        self._sampling_rate = sampling_rate