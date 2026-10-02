from models.catalog.catalog_item import CatalogItem

class RAM(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, capacity, type, frequency, modules, latency, voltage):
        super().__init__(code, name, price, description, brand, stock)
        self._capacity = capacity
        self._type = type
        self._frequency = frequency
        self._modules = modules
        self._latency = latency
        self._voltage = voltage