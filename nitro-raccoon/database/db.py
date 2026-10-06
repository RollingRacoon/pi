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
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    item_type VARCHAR(20) NOT NULL,
    description TEXT NOT NULL,
    brand VARCHAR(50) NOT NULL,
    stock INT NOT NULL,
    adapter_type VARCHAR(50),
    air_cooler_type VARCHAR(50),
    cable_type VARCHAR(50),
    keyboard_type VARCHAR(50),
    microphone_type VARCHAR(50),
    mouse_pad_type VARCHAR(50),
    psu_type VARCHAR(50),
    ram_type VARCHAR(50),
    storage_type VARCHAR(50),
    water_cooler_type VARCHAR(50),
    item_connection VARCHAR(50),
    socket VARCHAR(50),
    socket_compatibility VARCHAR(255),
    chipset VARCHAR(50),
    interface VARCHAR(50),
    form_factor VARCHAR(50),
    pc_case_format VARCHAR(50),
    storage_format VARCHAR(50)
    size VARCHAR(50),
    lighting VARCHAR(50),
    material VARCHAR(50),
    length DECIMAL(10, 2),
    width DECIMAL(10, 2),
    thickness DECIMAL(10, 2),
    voltage DECIMAL(5, 2),
    capacity VARCHAR(50),
    frequency VARCHAR(50),
    input_connector VARCHAR(50),
    output_connector VARCHAR(50),
    source_interface VARCHAR(50),
    target_interface VARCHAR(50),
    compatibility VARCHAR(255),
    version VARCHAR(50),
    transfer_speed VARCHAR(50),
    max_power VARCHAR(50),
    max_resolution VARCHAR(50),
    requires_power_supply BOOLEAN,
    supported_tdp INT,
    fan_rotation VARCHAR(50),
    fan_number INT,
    radiator_size VARCHAR(50),
    cores INT,
    threads INT,
    base_frequency VARCHAR(50),
    turbo_frequency VARCHAR(50),
    cache VARCHAR(50),
    tdp INT,
    max_rpm INT,
    cfm DECIMAL(10, 2),
    static_pressure DECIMAL(10, 2),
    bearing_type VARCHAR(50),
    connector_type VARCHAR(50),
    noise_level DECIMAL(10, 2),
    led_number INT,
    vram VARCHAR(50),
    memory_type VARCHAR(50),
    clock VARCHAR(50),
    consumption INT,
    layout VARCHAR(50),
    switch VARCHAR(50),
    key_count INT,
    polar_pattern VARCHAR(50),
    sensitivity VARCHAR(50),
    sampling_rate VARCHAR(50),
    resolution VARCHAR(50),
    refresh_rate INT,
    response DECIMAL(10, 2),
    display_type VARCHAR(50),
    proportion VARCHAR(20),
    ram_slots INT,
    ram_capacity VARCHAR(50),
    m2_slots INT,
    pcie_slots INT,
    sensor VARCHAR(50),
    dpi INT,
    button_count INT,
    polling_rate INT,
    weight DECIMAL(10, 2),
    non_slip_base BOOLEAN,
    max_gpu_length DECIMAL(10, 2),
    max_cooler_height DECIMAL(10, 2),
    supported_radiator VARCHAR(100),
    panel_type VARCHAR(50),
    potency INT,
    certification VARCHAR(50),
    modularity VARCHAR(50),
    fan VARCHAR(50),
    connectors VARCHAR(255),
    modules INT,
    latency VARCHAR(50),
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
        id INT AUTO_INCREMENT PRIMARY KEY,
        code VARCHAR(50) NOT NULL UNIQUE,
        user_name VARCHAR(100) NOT NULL,
        rating_score DECIMAL(2, 1),
        FOREIGN KEY (id) REFERENCES items_catalog(id)
    )
    """
    cursor.execute(create_ratings)
    connection.commit()
    connection.close()


def create_item(code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
            INSERT INTO items_catalog(code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (code, name, price, item_type, description, brand, stock, adapter_type, air_cooler_type, cable_type, keyboard_type, microphone_type, mouse_pad_type, psu_type, ram_type, storage_type, water_cooler_type, item_connection, socket, socket_compatibility, chipset, interface, form_factor, pc_case_format, storage_format, size, lighting, material, length, width, thickness, voltage, capacity, frequency, input_connector, output_connector, source_interface, target_interface, compatibility, version, transfer_speed, max_power, max_resolution, requires_power_supply, supported_tdp, fan_rotation, fan_number, radiator_size, cores, threads, base_frequency, turbo_frequency, cache, tdp, max_rpm, cfm, static_pressure, bearing_type, connector_type, noise_level, led_number, vram, memory_type, clock, consumption, layout, switch, key_count, polar_pattern, sensitivity, sampling_rate, resolution, refresh_rate, response, display_type, proportion, ram_slots, ram_capacity, m2_slots, pcie_slots, sensor, dpi, button_count, polling_rate, weight, non_slip_base, max_gpu_length, max_cooler_height, supported_radiator, panel_type, potency, certification, modularity, fan, connectors, modules, latency, reading_speed, writing_speed)
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

def create_user_rating(code, user_name, rating_score):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO ratings(code, user_name, rating_score)
        VALUES (%s, %s, %s)
""", (code, user_name, float(rating_score)))
    connection.commit()
    connection.close()

def list_ratings():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT ratings.id, items_catalog.name, ratings.user_name, ratings.rating_score
    FROM ratings
    JOIN items_catalog ON ratings.id = items_catalog.id
    """)
    ratings = cursor.fetchall()
    for rating in ratings:
        print(rating)
    connection.commit()
    connection.close()