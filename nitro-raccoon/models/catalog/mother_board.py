from models.catalog.catalog_item import CatalogItem

class MotherBoard(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, socket, chipset, form_factor, ram_type, ram_slots, ram_capacity, m2_slots, pcie_slots):
        super().__init__(code, name, price, description, brand, stock)
        self._socket = socket
        self._chipset = chipset
        self._form_factor = form_factor
        self._ram_type = ram_type
        self._ram_slots = ram_slots
        self._ram_capacity = ram_capacity
        self._m2_slots = m2_slots
        self._pcie_slots = pcie_slots