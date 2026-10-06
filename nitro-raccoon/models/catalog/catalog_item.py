class CatalogItem:
    def __init__(self, code, name, item_type, price, description, brand, stock):
        self._code = code
        self._item_type = item_type        
        self._name = name
        self._price = price
        self._description = description
        self.brand = brand
        self.stock = stock
        self._avaliacao = []

    def __str__(self):
        return self._name

    def define_stock(self, new_stock):
        if new_stock not in CatalogItem.VALID_STATUS:
            raise ValueError(f'Status inválido: {new_stock}')
        self.stock = new_stock