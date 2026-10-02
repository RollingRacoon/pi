from models.catalog.catalog_item import CatalogItem

class Storage(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, type, capacity, interface, reading_speed, writing_speed, format):
        super().__init__(code, name, price, description, brand, stock)
        self._type = type
        self._capacity = capacity
        self._interface = interface
        self._reading_speed = reading_speed
        self._writing_speed = writing_speed
        self._format = format