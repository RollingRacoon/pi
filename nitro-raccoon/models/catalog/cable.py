from models.catalog.catalog_item import CatalogItem

class Cable(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, type, input_connector, output_connector, length, version, transfer_speed, max_power, max_resolution, material):
        super().__init__(code, name, price, description, brand, stock)
        self._type = type
        self._input_connector = input_connector
        self._output_connector = output_connector
        self._length = length
        self._version = version
        self._transfer_speed = transfer_speed
        self._max_power = max_power
        self._max_resolution = max_resolution
        self._material = material