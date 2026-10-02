from models.catalog.catalog_item import CatalogItem

class CPU(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, socket, cores, threads, base_frequency, turbo_frequency, cache, tdp):
        super().__init__(code, name, price, description, brand, stock)
        self._socket = socket
        self._cores = cores
        self._threads = threads
        self._base_frequency = base_frequency
        self._turbo_frequency = turbo_frequency
        self._cache = cache
        self._tdp = tdp