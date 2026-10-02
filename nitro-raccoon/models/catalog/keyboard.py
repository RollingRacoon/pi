from models.catalog.catalog_item import CatalogItem

class Keyboard(CatalogItem):
    def __init__(self, code, name, price, description, brand, stock, type, conexao, layout, switch, key_count, lighting):
        super().__init__(code, name, price, description, brand, stock)
        self._type = type
        self._conexao = conexao
        self._layout = layout
        self._switch = switch
        self._key_count = key_count
        self._lighting = lighting