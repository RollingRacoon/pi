from models.rating import Rating

class CatalogItem:
    _catalogo = []
    STATUS_VALIDO = ('pendente','em estoque','esgotado')

    def __init__(self, code, name, item_type, price, description, brand, stock):
        self._code = code
        self._item_type = item_type        
        self._name = name
        self._price = price
        self._description = description
        self.brand = brand
        self.stock = stock
        self._avaliacoes = []
        CatalogItem._catalogo.append(self)

    def __str__(self):
        return f'{self._code} | {self._name}, {self._item_type} - {self.brand} | Preço: R${self._price} | {self.stock}\n| {self._description}'

    def define_stock(self, new_stock):
        if new_stock not in CatalogItem.VALID_STATUS:
            raise ValueError(f'Status inválido: {new_stock}')
        self.stock = new_stock

    @classmethod
    def list_items(cls):
        for item in cls.catalog:
            print(
                item.code.ljust(10)
                + item.name.ljust(15)
                + item.item_type.ljust(10)
                + item.brand.ljust(10)
                + item.price.ljust(10)
                + item.stock(20)
                + item.description.ljust(10)
            )

    def receive_rating(self, costumer, score):
        rating = Rating(costumer, score)
        self._avaliacoes.append(rating)

    @property
    def rating_average(self):
        if not self._avaliacoes:
            return 0
        soma = sum(rating._score for rating in self._avaliacoes)
        average = soma / len(self._avaliacoes)
        return round(average, 1)

    def add_to_catalog(self, item):
        if isinstance(item, CatalogItem):
            self._catalogo.append(item)
        else:
            raise ValueError('Só é possível adicionar itens do tipo CatalogItem (ou subclasses).')

    @property
    def show_catalog(self):
        print(f'Catálogo de {self._name}')
        for index, item in enumerate(self._catalogo, start=1):
            line = f'{index}. {self._name} - R${self._price}'
            if hasattr(item, 'adapter_type'):
                line += f' | : {item._adapter_type}'
            if hasattr(item, 'air_cooler_type'):
                line += f' | : {item._air_cooler_type}'
            if hasattr(item, 'cable_type'):
                line += f' | : {item._cable_type}'
            if hasattr(item, 'cores'):
                line += f' | : {item._cores}'
            if hasattr(item, 'bearing_type'):
                line += f' | : {item._bearing_type}'
            if hasattr(item, 'vram'):
                line += f' | : {item._vram}'
            if hasattr(item, 'keyboard_type'):
                line += f' | : {item._keyboard_type}'
            if hasattr(item, 'microphone_type'):
                line += f' | : {item._microphone_type}'
            if hasattr(item, 'refresh_rate'):
                line += f' | : {item._refresh_rate}'
            if hasattr(item, 'm2_slots'):
                line += f' | : {item._m2_slots}'
            if hasattr(item, 'mouse_pad_type'):
                line += f' | : {item._mouse_pad_type}'
            if hasattr(item, 'dpi'):
                line += f' | : {item._dpi}'
            if hasattr(item, 'pc_case_format'):
                line += f' | : {item._pc_case_format}'
            if hasattr(item, 'psu_type'):
                line += f' | : {item._psu_type}'
            if hasattr(item, 'modules'):
                line += f' | : {item._modules}'
            if hasattr(item, 'storage_type'):
                line += f' | : {item._storage_type}'
            if hasattr(item, 'water_cooler_type'):
                line += f' | : {item._water_cooler_type}'
            print(line)