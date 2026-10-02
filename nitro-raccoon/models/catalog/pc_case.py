from models.catalog.catalog_item import CatalogItem

class PCCase(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, format, form_factor, max_gpu_length, max_cooler_height, supported_radiator, fan_number, panel_type):
        super().__init__(code, name, price, description, brand, stock)
        self._format = format
        self._form_factor = form_factor
        self._max_gpu_length = max_gpu_length
        self._max_cooler_height = max_cooler_height
        self._supported_radiator = supported_radiator
        self._fan_number = fan_number
        self._panel_type = panel_type