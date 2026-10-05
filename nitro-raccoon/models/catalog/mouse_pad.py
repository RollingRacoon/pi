from models.catalog.catalog_item import CatalogItem

class MousePad(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, material, length, width, thickness, mouse_pad_type, non_slip_base):
        super().__init__(code, name, price, description, brand, stock)
        self._material = material
        self._length = length
        self._width = width
        self._thickness = thickness
        self._mouse_pad_type = mouse_pad_type
        self._non_slip_base = non_slip_base