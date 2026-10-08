import mysql.connector

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nitro-raccoon"
    )
    return connection

def create_catalog():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items_catalog (
    items_id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    item_type VARCHAR(20) NOT NULL,
    description TEXT NOT NULL,
    brand VARCHAR(50) NOT NULL,
    stock INT NOT NULL,
    adapter_type VARCHAR(20),
    air_cooler_type VARCHAR(20),
    cable_type VARCHAR(20),
    keyboard_type VARCHAR(20),
    microphone_type VARCHAR(20),
    mouse_pad_type VARCHAR(20),
    psu_type VARCHAR(20),
    ram_type VARCHAR(20),
    storage_type VARCHAR(20),
    water_cooler_type VARCHAR(20),
    item_connection VARCHAR(20),
    socket VARCHAR(20),
    socket_compatibility VARCHAR(60),
    chipset VARCHAR(30),
    interface VARCHAR(20),
    form_factor VARCHAR(20),
    pc_case_format VARCHAR(20),
    storage_format VARCHAR(20),
    size VARCHAR(20),
    lighting VARCHAR(20),
    material VARCHAR(30),
    length DECIMAL(10, 2),
    width DECIMAL(10, 2),
    thickness DECIMAL(10, 2),
    voltage DECIMAL(5, 2),
    capacity VARCHAR(20),
    frequency VARCHAR(20),
    input_connector VARCHAR(25),
    output_connector VARCHAR(25),
    source_interface VARCHAR(25),
    target_interface VARCHAR(25),
    compatibility VARCHAR(60),
    version VARCHAR(20),
    transfer_speed VARCHAR(20),
    max_power VARCHAR(20),
    max_resolution VARCHAR(20),
    requires_power_supply BOOLEAN,
    supported_tdp INT,
    fan_rotation VARCHAR(20),
    fan_number INT,
    radiator_size VARCHAR(20),
    cores INT,
    threads INT,
    base_frequency VARCHAR(20),
    turbo_frequency VARCHAR(20),
    cache VARCHAR(20),
    tdp INT,
    max_rpm INT,
    cfm DECIMAL(10, 2),
    static_pressure DECIMAL(10, 2),
    bearing_type VARCHAR(20),
    connector_type VARCHAR(20),
    noise_level DECIMAL(10, 2),
    led_number INT,
    vram VARCHAR(20),
    memory_type VARCHAR(20),
    clock VARCHAR(20),
    consumption INT,
    layout VARCHAR(20),
    switch VARCHAR(25),
    key_count INT,
    polar_pattern VARCHAR(20),
    sensitivity VARCHAR(20),
    sampling_rate VARCHAR(20),
    resolution VARCHAR(20),
    refresh_rate INT,
    response DECIMAL(10, 2),
    display_type VARCHAR(20),
    proportion VARCHAR(20),
    ram_slots INT,
    ram_capacity VARCHAR(20),
    m2_slots INT,
    pcie_slots INT,
    sensor VARCHAR(25),
    dpi INT,
    button_count INT,
    polling_rate INT,
    weight DECIMAL(10, 2),
    non_slip_base BOOLEAN,
    max_gpu_length DECIMAL(10, 2),
    max_cooler_height DECIMAL(10, 2),
    supported_radiator VARCHAR(30),
    panel_type VARCHAR(20),
    potency INT,
    certification VARCHAR(20),
    modularity VARCHAR(20),
    fan VARCHAR(20),
    connectors VARCHAR(100),
    modules INT,
    latency VARCHAR(20),
    reading_speed INT,
    writing_speed INT
    )
    """)
    connection.commit()
    connection.close()

def create_ratings():
    connection = connect()
    cursor = connection.cursor()
    create_ratings = """
    CREATE TABLE IF NOT EXISTS items_catalog(
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(20) NOT NULL UNIQUE,
        name VARCHAR(100) NOT NULL,
        rating_score DECIMAL(2, 1),
        FOREIGN KEY (items_id) REFERENCES items_catalog(items_id)
    )
    """
    cursor.execute(create_ratings)
    connection.commit()
    connection.close()


def create_item(items_id, code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
            INSERT INTO items_catalog(items_id, code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (items_id, code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
    )
    connection.commit()
    connection.close()

def list_items():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
            SELECT * FROM items_catalog
        """
    )
    items_catalog = cursor.fetchall()
    for item in items_catalog:
        print(item)
    connection.commit()
    connection.close()



def list_ratings():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT ratings.user_id, items_catalog.name, ratings.name, ratings.rating_score
    FROM ratings
    JOIN items_catalog ON ratings.user_id = items_catalog.items_id
    """)
    ratings = cursor.fetchall()
    for rating in ratings:
        print(rating)
    connection.commit()
    connection.close()