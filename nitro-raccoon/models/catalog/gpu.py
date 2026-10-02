from models.catalog.catalog_item import CatalogItem

class GPU(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, chipset, vram, memory_type, clock, interface, consumption, length):
        super().__init__(code, name, price, description, brand, stock)
        self._chipset = chipset
        self._vram = vram
        self._memory_type = memory_type
        self._clock = clock
        self._interface = interface
        self._consumption = consumption
        self._length = length