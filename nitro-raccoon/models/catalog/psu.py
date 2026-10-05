from models.catalog.catalog_item import CatalogItem

class PSU(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, potency, certification, modularity, psu_type, fan, connectors):
        super().__init__(code, name, price, description, brand, stock)
        self._potency = potency
        self._certification = certification
        self._modularity = modularity
        self._psu_type = psu_type
        self._fan = fan
        self._connectors = connectors