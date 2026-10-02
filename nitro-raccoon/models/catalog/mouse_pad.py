from models.catalog.catalog_item import CatalogItem

class MousePad(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, material, lenght, width, thickness, surface, non_slip_base):
        super().__init__(code, name, price, description, brand, stock)
        self._material = material
        self._lenght = lenght
        self._width = width
        self._thickness = thickness
        self._surface = surface
        self._non_slip_base = non_slip_base