from decimal import Decimal, InvalidOperation

from models.rating import Rating


class CatalogItem:
    STATUS_VALIDO = ('pendente', 'em estoque', 'esgotado')
    # Itens aprovados: são os que aparecem no painel e na página inicial.
    STATUS_ATIVOS = ('em estoque', 'esgotado')

    ITEM_TYPES = (
        'adapter', 'air_cooler', 'cable', 'cpu', 'fan', 'gpu', 'keyboard',
        'microphone', 'monitor', 'mother_board', 'mouse', 'mouse_pad',
        'pc_case', 'psu', 'ram', 'storage', 'water_cooler',
    )

    # Mesmas colunas de especificação de items_catalog (database/db.py), na mesma ordem.
    SPEC_FIELDS = (
        'adapter_type', 'air_cooler_type', 'cable_type', 'keyboard_type',
        'microphone_type', 'mouse_pad_type', 'psu_type', 'ram_type',
        'storage_type', 'water_cooler_type', 'item_connection', 'socket',
        'socket_compatibility', 'chipset', 'interface', 'form_factor',
        'pc_case_format', 'storage_format', 'size', 'lighting',
        'material', 'length', 'width', 'thickness',
        'voltage', 'capacity', 'frequency', 'input_connector',
        'output_connector', 'source_interface', 'target_interface', 'compatibility',
        'version', 'transfer_speed', 'max_power', 'max_resolution',
        'requires_power_supply', 'supported_tdp', 'fan_rotation', 'fan_number',
        'radiator_size', 'cores', 'threads', 'base_frequency',
        'turbo_frequency', 'cache', 'tdp', 'max_rpm',
        'cfm', 'static_pressure', 'bearing_type', 'connector_type',
        'noise_level', 'led_number', 'vram', 'memory_type',
        'clock', 'consumption', 'layout', 'switch',
        'key_count', 'polar_pattern', 'sensitivity', 'sampling_rate',
        'resolution', 'refresh_rate', 'response', 'display_type',
        'proportion', 'ram_slots', 'ram_capacity', 'm2_slots',
        'pcie_slots', 'sensor', 'dpi', 'button_count',
        'polling_rate', 'weight', 'non_slip_base', 'max_gpu_length',
        'max_cooler_height', 'supported_radiator', 'panel_type', 'potency',
        'certification', 'modularity', 'fan', 'connectors',
        'modules', 'latency', 'reading_speed', 'writing_speed',
    )

    # Tipos das colunas numéricas / booleanas; todas as outras são texto.
    INT_FIELDS = frozenset({
        'supported_tdp', 'fan_number', 'cores', 'threads', 'tdp', 'max_rpm',
        'led_number', 'consumption', 'key_count', 'refresh_rate', 'ram_slots',
        'm2_slots', 'pcie_slots', 'dpi', 'button_count', 'polling_rate',
        'potency', 'modules', 'reading_speed', 'writing_speed',
    })
    DECIMAL_FIELDS = frozenset({
        'length', 'width', 'thickness', 'voltage', 'cfm', 'static_pressure',
        'noise_level', 'response', 'weight', 'max_gpu_length', 'max_cooler_height',
    })
    BOOL_FIELDS = frozenset({'requires_power_supply', 'non_slip_base'})

    def __init__(self, code, name, item_type, price, description, brand,
                 stock='pendente', **specs):
        unknown = set(specs) - set(self.SPEC_FIELDS)
        if unknown:
            raise ValueError(f'Campos desconhecidos: {", ".join(sorted(unknown))}')

        self.id = None
        self.code = code
        self.name = name
        self.item_type = item_type
        self.price = self._decimal(price, 'preço')
        self.description = description
        self.brand = brand
        self.define_stock(stock)
        self.ratings = []

        # Só guarda o que foi preenchido; cada valor já sai convertido para o tipo da coluna.
        self.specs = {}
        for field, value in specs.items():
            if isinstance(value, str):
                value = value.strip()
            if value is None or value == '':
                continue
            self.specs[field] = self._normalize(field, value)

    # Permite item.cores, item.socket etc. (Jinja e código em geral).
    def __getattr__(self, name):
        specs = self.__dict__.get('specs')
        if specs is not None and name in specs:
            return specs[name]
        raise AttributeError(name)

    def __str__(self):
        return (f'{self.code} | {self.name}, {self.item_type} - {self.brand} '
                f'| Preço: R${self.price} | {self.stock}\n| {self.description}')

    @staticmethod
    def _decimal(value, label):
        try:
            number = Decimal(str(value).strip().replace(',', '.'))
        except InvalidOperation:
            raise ValueError(f'O campo "{label}" precisa ser um número.') from None
        if not number.is_finite() or number < 0:
            raise ValueError(f'O campo "{label}" precisa ser um número maior ou igual a zero.')
        return number

    @classmethod
    def _normalize(cls, field, value):
        if field in cls.BOOL_FIELDS:
            text = str(value).strip().lower()
            if text in ('sim', '1', 'true'):
                return True
            if text in ('não', 'nao', '0', 'false'):
                return False
            raise ValueError(f'O campo "{field}" aceita apenas Sim ou Não.')
        if field in cls.INT_FIELDS:
            number = cls._decimal(value, field)
            if number != number.to_integral_value():
                raise ValueError(f'O campo "{field}" precisa ser um número inteiro.')
            return int(number)
        if field in cls.DECIMAL_FIELDS:
            return cls._decimal(value, field)
        return str(value).strip()

    def define_stock(self, new_stock):
        if new_stock not in self.STATUS_VALIDO:
            raise ValueError(f'Estoque inválido: {new_stock}')
        self.stock = new_stock

    @property
    def is_active(self):
        return self.stock in self.STATUS_ATIVOS

    def receive_rating(self, costumer, score):
        self.ratings.append(Rating(costumer, score))

    @property
    def rating_average(self):
        if not self.ratings:
            return 0
        return round(sum(rating.score for rating in self.ratings) / len(self.ratings), 1)