from models.catalog.catalog_item import CatalogItem

class Fan(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, size, max_rpm, cfm, static_pressure, bearing_type, connector_type, lighting, noise_level, led_number, voltage):
        super().__init__(code, name, price, description, brand, stock)
        self._size = size
        self._max_rpm = max_rpm
        self._cfm = cfm        
        self._static_pressure = static_pressure        
        self._bearing_type = bearing_type        
        self._connector_type = connector_type
        self._lighting = lighting
        self._noise_level = noise_level
        self._led_number = led_number
        self._voltage = voltage