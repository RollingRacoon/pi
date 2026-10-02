from models.catalog.catalog_item import CatalogItem

class WaterCooler(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, type, socket_compatibility, supported_tdp, fan_rotation, radiator_size, fan_number):
        super().__init__(code, name, price, description, brand, stock)
        self._type = type
        self._socket_compatibility = socket_compatibility
        self._supported_tdp = supported_tdp
        self._fan_rotation = fan_rotation
        self._radiator_size = radiator_size
        self._fan_number = fan_number