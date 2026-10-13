# Funções e tabelas de apoio usadas pelos templates HTML (Jinja).
import math

# Nome de cada categoria no singular, em português (para exibir na tela).
TYPE_SINGULAR = {
    'cpu': 'Processador', 'mother_board': 'Placa-mãe', 'gpu': 'Placa de vídeo',
    'ram': 'Memória RAM', 'storage': 'Armazenamento', 'psu': 'Fonte',
    'pc_case': 'Gabinete', 'air_cooler': 'Air cooler', 'water_cooler': 'Water cooler',
    'fan': 'Ventoinha', 'monitor': 'Monitor', 'keyboard': 'Teclado',
    'mouse': 'Mouse', 'mouse_pad': 'Mousepad', 'microphone': 'Microfone',
    'adapter': 'Adaptador', 'cable': 'Cabo',
}

# O mesmo, no plural (títulos de seção).
TYPE_PLURAL = {
    'cpu': 'Processadores', 'mother_board': 'Placas-mãe', 'gpu': 'Placas de vídeo',
    'ram': 'Memórias RAM', 'storage': 'Armazenamento', 'psu': 'Fontes',
    'pc_case': 'Gabinetes', 'air_cooler': 'Air coolers', 'water_cooler': 'Water coolers',
    'fan': 'Ventoinhas', 'monitor': 'Monitores', 'keyboard': 'Teclados',
    'mouse': 'Mouses', 'mouse_pad': 'Mousepads', 'microphone': 'Microfones',
    'adapter': 'Adaptadores', 'cable': 'Cabos',
}

# Texto amigável para cada status de estoque.
STOCK_LABELS = {'em estoque': 'Em estoque', 'esgotado': 'Esgotado', 'pendente': 'Pendente'}

# Ficha técnica de cada categoria: quais campos mostrar, em que ordem e com qual unidade.
# (campo, rótulo, unidade)
SPEC_FIELDS = {
    'cpu': [('socket', 'Soquete', ''), ('cores', 'Núcleos', ''), ('threads', 'Threads', ''),
            ('base_frequency', 'Frequência base', 'GHz'), ('turbo_frequency', 'Frequência turbo', 'GHz'),
            ('cache', 'Cache', 'MB'), ('tdp', 'TDP', 'W')],
    'mother_board': [('socket', 'Soquete', ''), ('chipset', 'Chipset', ''), ('form_factor', 'Formato', ''),
                     ('ram_type', 'Tipo de memória', ''), ('ram_slots', 'Slots de RAM', ''),
                     ('ram_capacity', 'Capacidade máxima de RAM', 'GB'), ('m2_slots', 'Slots M.2', ''),
                     ('pcie_slots', 'Slots PCIe', '')],
    'gpu': [('chipset', 'Chipset', ''), ('vram', 'VRAM', 'GB'), ('memory_type', 'Tipo de memória', ''),
            ('clock', 'Clock', 'MHz'), ('consumption', 'Consumo', 'W'),
            ('length', 'Comprimento', 'mm'), ('interface', 'Interface', '')],
    'ram': [('ram_type', 'Tipo', ''), ('capacity', 'Capacidade', 'GB'), ('frequency', 'Frequência', 'MHz'),
            ('latency', 'Latência', ''), ('voltage', 'Tensão', 'V'), ('modules', 'Módulos', '')],
    'storage': [('storage_type', 'Tipo', ''), ('capacity', 'Capacidade', 'GB'), ('interface', 'Interface', ''),
                ('storage_format', 'Formato', ''), ('reading_speed', 'Leitura', 'MB/s'),
                ('writing_speed', 'Gravação', 'MB/s')],
    'psu': [('psu_type', 'Tipo', ''), ('potency', 'Potência', 'W'), ('certification', 'Certificação', ''),
            ('modularity', 'Modularidade', ''), ('form_factor', 'Formato', ''),
            ('fan', 'Ventoinha', ''), ('connectors', 'Conectores', '')],
    'pc_case': [('pc_case_format', 'Formato do gabinete', ''), ('form_factor', 'Placas-mãe suportadas', ''),
                ('max_gpu_length', 'Comprimento máx. da GPU', 'mm'), ('max_cooler_height', 'Altura máx. do cooler', 'mm'),
                ('supported_radiator', 'Radiadores suportados', ''), ('panel_type', 'Painel lateral', ''),
                ('fan', 'Ventoinhas incluídas', '')],
    'air_cooler': [('air_cooler_type', 'Tipo', ''), ('socket_compatibility', 'Soquetes compatíveis', ''),
                   ('supported_tdp', 'TDP suportado', 'W'), ('size', 'Altura', 'mm'),
                   ('fan_number', 'Quantidade de ventoinhas', ''), ('fan_rotation', 'Rotação', 'RPM'),
                   ('noise_level', 'Ruído', 'dB'), ('lighting', 'Iluminação', '')],
    'water_cooler': [('water_cooler_type', 'Tipo', ''), ('radiator_size', 'Radiador', ''),
                     ('socket_compatibility', 'Soquetes compatíveis', ''), ('supported_tdp', 'TDP suportado', 'W'),
                     ('fan_number', 'Quantidade de ventoinhas', ''), ('fan_rotation', 'Rotação', 'RPM'),
                     ('lighting', 'Iluminação', '')],
    'fan': [('size', 'Tamanho', ''), ('max_rpm', 'Rotação máxima', 'RPM'), ('cfm', 'Fluxo de ar', 'CFM'),
            ('static_pressure', 'Pressão estática', 'mmH₂O'), ('bearing_type', 'Rolamento', ''),
            ('connector_type', 'Conector', ''), ('noise_level', 'Ruído', 'dB'),
            ('led_number', 'Quantidade de LEDs', ''), ('lighting', 'Iluminação', '')],
    'monitor': [('size', 'Tamanho', 'pol.'), ('resolution', 'Resolução', ''),
                ('refresh_rate', 'Taxa de atualização', 'Hz'), ('response', 'Tempo de resposta', 'ms'),
                ('display_type', 'Tipo de painel', ''), ('proportion', 'Proporção', ''),
                ('item_connection', 'Conexões', '')],
    'keyboard': [('keyboard_type', 'Tipo', ''), ('layout', 'Layout', ''), ('switch', 'Switch', ''),
                 ('key_count', 'Quantidade de teclas', ''), ('form_factor', 'Formato', ''),
                 ('item_connection', 'Conexão', ''), ('lighting', 'Iluminação', '')],
    'mouse': [('sensor', 'Sensor', ''), ('dpi', 'DPI máximo', ''), ('button_count', 'Quantidade de botões', ''),
              ('polling_rate', 'Taxa de polling', 'Hz'), ('weight', 'Peso', 'g'),
              ('item_connection', 'Conexão', ''), ('lighting', 'Iluminação', '')],
    'mouse_pad': [('mouse_pad_type', 'Tipo', ''), ('size', 'Tamanho', ''), ('width', 'Largura', 'mm'),
                  ('length', 'Comprimento', 'mm'), ('thickness', 'Espessura', 'mm'),
                  ('material', 'Material', ''), ('non_slip_base', 'Base antiderrapante', '')],
    'microphone': [('microphone_type', 'Tipo', ''), ('polar_pattern', 'Padrão polar', ''),
                   ('sensitivity', 'Sensibilidade', ''), ('sampling_rate', 'Taxa de amostragem', 'kHz'),
                   ('frequency', 'Resposta de frequência', ''), ('item_connection', 'Conexão', '')],
    'adapter': [('adapter_type', 'Tipo', ''), ('input_connector', 'Conector de entrada', ''),
                ('output_connector', 'Conector de saída', ''), ('source_interface', 'Interface de origem', ''),
                ('target_interface', 'Interface de destino', ''), ('compatibility', 'Compatibilidade', ''),
                ('version', 'Versão', ''), ('transfer_speed', 'Velocidade de transferência', ''),
                ('max_power', 'Potência máxima', 'W'), ('max_resolution', 'Resolução máxima', ''),
                ('requires_power_supply', 'Exige fonte externa', '')],
    'cable': [('cable_type', 'Tipo', ''), ('length', 'Comprimento', 'm'), ('connector_type', 'Conectores', ''),
              ('version', 'Versão', ''), ('transfer_speed', 'Velocidade de transferência', ''),
              ('material', 'Material', '')],
}


def brl(value):
    # Formata um número como moeda brasileira: 1234.5 -> "R$ 1.234,50".
    try:
        v = float(value)
    except (TypeError, ValueError):
        v = 0.0  # valor inválido vira R$ 0,00 em vez de quebrar a página
    # Troca os separadores do padrão americano (1,234.50) pelo brasileiro.
    return 'R$ ' + f'{v:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')


def _number(text):
    """'4.2' -> '4,2'; '1000.0' -> '1000'. Texto não numérico volta igual."""
    try:
        f = float(text)
    except ValueError:
        return text
    if not math.isfinite(f):
        return text
    return str(int(f)) if f == int(f) else str(f).replace('.', ',')


def _get(item, field):
    # Pega o valor de uma especificação, olhando primeiro o dicionário `specs`.
    specs = getattr(item, 'specs', None)
    if isinstance(specs, dict) and field in specs:
        return specs[field]
    return getattr(item, field, None)


# Campos Sim/Não, exibidos como texto em vez de 1/0.
BOOL_FIELDS = {'non_slip_base', 'requires_power_supply'}


def spec_rows(item):
    """Lista de (rótulo, texto) só com os campos preenchidos da ficha técnica."""
    rows = []
    # Percorre os campos da categoria do item, na ordem definida em SPEC_FIELDS.
    for field, label, unit in SPEC_FIELDS.get(getattr(item, 'item_type', None), []):
        value = _get(item, field)
        if value is None or str(value).strip() == '':
            continue  # campo não preenchido não aparece
        text = str(value).strip()
        if field in BOOL_FIELDS:
            text = 'Sim' if text.lower() in ('1', 'true', 'sim') else 'Não'
        if unit:
            text = f'{_number(text)} {unit}'
        rows.append((label, text))
    return rows


def init_app(app):
    # Registra tudo no Flask: o filtro `brl` ({{ preco|brl }}) e as variáveis
    # globais que os templates podem usar sem receber da rota.
    app.add_template_filter(brl, 'brl')
    app.jinja_env.globals.update(
        spec_rows=spec_rows,
        type_singular=TYPE_SINGULAR,
        type_plural=TYPE_PLURAL,
        stock_labels=STOCK_LABELS,
    )