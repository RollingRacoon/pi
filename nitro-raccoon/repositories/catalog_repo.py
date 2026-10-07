from database.db import connect
from models.catalog.catalog_item import CatalogItem
from models.catalog.adapter import Adapter
from models.catalog.air_cooler import AirCooler
from models.catalog.cable import Cable
from models.catalog.cpu import CPU
from models.catalog.fan import Fan
from models.catalog.gpu import GPU
from models.catalog.keyboard import Keyboard
from models.catalog.microphone import Microphone
from models.catalog.monitor import Monitor
from models.catalog.mother_board import MotherBoard
from models.catalog.mouse import Mouse
from models.catalog.mouse_pad import MousePad
from models.catalog.pc_case import PCCase
from models.catalog.psu import PSU
from models.catalog.ram import RAM
from models.catalog.storage import Storage
from models.catalog.water_cooler import WaterCooler

def save(item):
    # Todas as variáveis começam como None; cada tipo preenche só as suas
    adapter_type = air_cooler_type = cable_type = keyboard_type = microphone_type = None
    mouse_pad_type = psu_type = ram_type = storage_type = water_cooler_type = None
    item_connection = socket = socket_compatibility = chipset = interface = None
    form_factor = pc_case_format = storage_format = size = lighting = material = None
    length = width = thickness = voltage = capacity = frequency = None
    input_connector = output_connector = source_interface = target_interface = None
    compatibility = version = transfer_speed = max_power = max_resolution = None
    requires_power_supply = None
    supported_tdp = fan_rotation = fan_number = radiator_size = None
    cores = threads = base_frequency = turbo_frequency = cache = tdp = None
    max_rpm = cfm = static_pressure = bearing_type = connector_type = None
    noise_level = led_number = None
    vram = memory_type = clock = consumption = None
    layout = switch = key_count = None
    polar_pattern = sensitivity = sampling_rate = None
    resolution = refresh_rate = response = display_type = proportion = None
    ram_slots = ram_capacity = m2_slots = pcie_slots = None
    sensor = dpi = button_count = polling_rate = weight = None
    non_slip_base = None
    max_gpu_length = max_cooler_height = supported_radiator = panel_type = None
    potency = certification = modularity = fan = connectors = None
    modules = latency = None
    reading_speed = writing_speed = None

    if isinstance(item, Adapter):
        item_type = 'adapter'
        adapter_type = item._adapter_type
        input_connector = item._input_connector
        output_connector = item._output_connector
        source_interface = item._source_interface
        target_interface = item._target_interface
        compatibility = item._compatibility
        version = item._version
        transfer_speed = item._transfer_speed
        max_power = item._max_power
        max_resolution = item._max_resolution
        requires_power_supply = item._requires_power_supply
    elif isinstance(item, AirCooler):
        item_type = 'air_cooler'
        air_cooler_type = item._air_cooler_type
        socket_compatibility = item._socket_compatibility
        supported_tdp = item._supported_tdp
        fan_rotation = item._fan_rotation
        fan_number = item._fan_number
    elif isinstance(item, Cable):
        item_type = 'cable'
        cable_type = item._cable_type
        input_connector = item._input_connector
        output_connector = item._output_connector
        length = item._length
        version = item._version
        transfer_speed = item._transfer_speed
        max_power = item._max_power
        max_resolution = item._max_resolution
        material = item._material
    elif isinstance(item, CPU):
        item_type = 'cpu'
        socket = item._socket
        cores = item._cores
        threads = item._threads
        base_frequency = item._base_frequency
        turbo_frequency = item._turbo_frequency
        cache = item._cache
        tdp = item._tdp
    elif isinstance(item, Fan):
        item_type = 'fan'
        size = item._size
        max_rpm = item._max_rpm
        cfm = item._cfm
        static_pressure = item._static_pressure
        bearing_type = item._bearing_type
        connector_type = item._connector_type
        lighting = item._lighting
        noise_level = item._noise_level
        led_number = item._led_number
        voltage = item._voltage
    elif isinstance(item, GPU):
        item_type = 'gpu'
        chipset = item._chipset
        vram = item._vram
        memory_type = item._memory_type
        clock = item._clock
        interface = item._interface
        consumption = item._consumption
        length = item._length
    elif isinstance(item, Keyboard):
        item_type = 'keyboard'
        keyboard_type = item._keyboard_type
        item_connection = item._connection
        layout = item._layout
        switch = item._switch
        key_count = item._key_count
        lighting = item._lighting
    elif isinstance(item, Microphone):
        item_type = 'microphone'
        microphone_type = item._microphone_type
        polar_pattern = item._polar_pattern
        item_connection = item._connection
        frequency = item._frequency
        sensitivity = item._sensitivity
        sampling_rate = item._sampling_rate
    elif isinstance(item, Monitor):
        item_type = 'monitor'
        size = item._size
        resolution = item._resolution
        refresh_rate = item._refresh_rate
        response = item._response
        display_type = item._display_type
        proportion = item._proportion
        item_connection = item._connection
    elif isinstance(item, MotherBoard):
        item_type = 'mother_board'
        socket = item._socket
        chipset = item._chipset
        form_factor = item._form_factor
        ram_type = item._ram_type
        ram_slots = item._ram_slots
        ram_capacity = item._ram_capacity
        m2_slots = item._m2_slots
        pcie_slots = item._pcie_slots
    elif isinstance(item, MousePad):
        item_type = 'mouse_pad'
        material = item._material
        length = item._lenght
        width = item._width
        thickness = item._thickness
        mouse_pad_type = item._mouse_pad_type
        non_slip_base = item._non_slip_base
    elif isinstance(item, Mouse):
        item_type = 'mouse'
        sensor = item._sensor
        dpi = item._dpi
        button_count = item._button_count
        item_connection = item._connection
        polling_rate = item._polling_rate
        weight = item._weight
    elif isinstance(item, PCCase):
        item_type = 'pc_case'
        pc_case_format = item._format
        form_factor = item._form_factor
        max_gpu_length = item._max_gpu_length
        max_cooler_height = item._max_cooler_height
        supported_radiator = item._supported_radiator
        fan_number = item._fan_number
        panel_type = item._panel_type
    elif isinstance(item, PSU):
        item_type = 'psu'
        potency = item._potency
        certification = item._certification
        modularity = item._modularity
        psu_type = item._psu_type
        fan = item._fan
        connectors = item._connectors
    elif isinstance(item, RAM):
        item_type = 'ram'
        capacity = item._capacity
        ram_type = item._ram_type
        frequency = item._frequency
        modules = item._modules
        latency = item._latency
        voltage = item._voltage
    elif isinstance(item, Storage):
        item_type = 'storage'
        storage_type = item._storage_type
        capacity = item._capacity
        interface = item._interface
        reading_speed = item._reading_speed
        writing_speed = item._writing_speed
        storage_format = item._format
    elif isinstance(item, WaterCooler):
        item_type = 'water_cooler'
        water_cooler_type = item._water_cooler_type
        socket_compatibility = item._socket_compatibility
        supported_tdp = item._supported_tdp
        fan_rotation = item._fan_rotation
        radiator_size = item._radiator_size
        fan_number = item._fan_number
    else:
        raise ValueError('O item precisa estar de acordo com os parâmetros estabelecidos.')

    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO items_catalog
            (code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (item._code, item._name, item._price, item_type, item._description, item.brand, item.stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
    )
    connection.commit()
    connection.close()

def seek_by_items_id(items_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT items_id, name, item_type, stock "
        "FROM items_catalog WHERE items_id = %s",
        (items_id,)
    )
    line = cursor.fetchone()
    connection.close()

    if line is None:
        return None

    items_id, name, item_type, stock = line
    catalog_item = CatalogItem(name, item_type)
    catalog_item.define_stock(stock)
    catalog_item.items_id = items_id
    return catalog_item

def list_all():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT items_id, code, name, price, type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed"
    )
    lines = cursor.fetchall()
    connection.close()

    items_catalog = []
    for items_id, code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed in lines:
        item = CatalogItem(items_id, code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
        item.define_stock(stock)
        item.items_id = items_id
        items_catalog.append(item)
    return items_catalog

def list_by_category(item):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
    """
    SELECT code, item_type, name, price, description, brand, stock
    FROM catalog_item
    WHERE item_type = %s
    """, (item,)
)
    lines = cursor.fetchall()
    connection.close()

    items = []
    for code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed in lines:
        price = float(price)
        if item_type == 'adapter':
            items.append(Adapter(code, name, price, description, brand, stock, adapter_type, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply))
        elif item_type == 'air_cooler':
            items.append(AirCooler(code, name, price, description, brand, stock, air_cooler_type, socket_compatibility, supported_tdp, fan_rotation, fan_number))
        elif item_type == 'cable':
            items.append(Cable(code, name, price, description, brand, stock, cable_type, input_connector, output_connector, length, version, transfer_speed, max_power, max_resolution, material))
        elif item_type == 'cpu':
            items.append(CPU(code, name, price, description, brand, stock, socket, cores, threads, base_frequency, turbo_frequency, cache, tdp))
        elif item_type == 'fan':
            items.append(Fan(code, name, price, description, brand, stock, size, max_rpm, cfm, static_pressure, bearing_type, connector_type, lighting, noise_level, led_number, voltage))
        elif item_type == 'gpu':
            items.append(GPU(code, name, price, description, brand, stock, chipset, vram, memory_type, clock, interface, consumption, length))
        elif item_type == 'keyboard':
            items.append(Keyboard(code, name, price, description, brand, stock, keyboard_type, item_connection, layout, switch, key_count, lighting))
        elif item_type == 'microphone':
            items.append(Microphone(code, name, price, description, brand, stock, microphone_type, polar_pattern, item_connection, frequency, sensitivity, sampling_rate))
        elif item_type == 'monitor':
            items.append(Monitor(code, name, price, description, brand, stock, size, resolution, refresh_rate, response, display_type, proportion, item_connection))
        elif item_type == 'mother_board':
            items.append(MotherBoard(code, name, price, description, brand, stock, socket, chipset, form_factor, ram_type, ram_slots, ram_capacity, m2_slots, pcie_slots))
        elif item_type == 'mouse_pad':
            items.append(MousePad(code, name, price, description, brand, stock, material, length, width, thickness, mouse_pad_type, non_slip_base))
        elif item_type == 'mouse':
            items.append(Mouse(code, name, price, description, brand, stock, sensor, dpi, button_count, item_connection, polling_rate, weight))
        elif item_type == 'pc_case':
            items.append(PCCase(code, name, price, description, brand, stock, pc_case_format, form_factor, max_gpu_length, max_cooler_height, supported_radiator, fan_number, panel_type))
        elif item_type == 'psu':
            items.append(PSU(code, name, price, description, brand, stock, potency, certification, modularity, psu_type, fan, connectors))
        elif item_type == 'ram':
            items.append(RAM(code, name, price, description, brand, stock, capacity, ram_type, frequency, modules, latency, voltage))
        elif item_type == 'storage':
            items.append(Storage(code, name, price, description, brand, stock, storage_type, capacity, interface, reading_speed, writing_speed, storage_format))
        elif item_type == 'water_cooler':
            items.append(WaterCooler(code, name, price, description, brand, stock, water_cooler_type, socket_compatibility, supported_tdp, fan_rotation, radiator_size, fan_number))

def list_by_stock(stock):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT items_id, name, item_type, stock "
        "FROM items_catalog WHERE stock = %s",
        (stock,)
    )
    lines = cursor.fetchall()
    connection.close()

def update_stock(items_id, new_stock):
    if new_stock not in CatalogItem.STATUS_VALIDOS:
        raise ValueError(f'Estoque inválido: {new_stock}')
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE items_catalog SET stock = %s WHERE items_id = %s", (new_stock, items_id)
    )
    connection.commit()
    connection.close()

def list_complete(items_id):
    from repositories import rating_repo, catalog_repo

    catalog_item = seek_by_items_id(id)
    if catalog_item is None:
        return None

    for rating in rating_repo.list_score_by_item(items_id):
        catalog_item._avaliacao.append(rating)

    for item in catalog_repo.list_by_category(items_id):
        catalog_item.add_to_catalog(item)

    return catalog_item