import os

import mysql.connector


def connect():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "nitro-raccoon"),
    )


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
    stock VARCHAR(20) NOT NULL DEFAULT 'pendente',
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
    writing_speed INT,
    image VARCHAR(255)
    )
    """)

    # Bancos criados com a versão antiga têm `stock INT`, mas o app usa texto
    # ('pendente', 'em estoque', 'esgotado'). Converte uma única vez.
    cursor.execute(
        "SELECT DATA_TYPE FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'items_catalog' "
        "AND COLUMN_NAME = 'stock'"
    )
    row = cursor.fetchone()
    data_type = row[0] if row else 'varchar'
    if isinstance(data_type, (bytes, bytearray)):
        data_type = data_type.decode()
    if str(data_type).lower() != 'varchar':
        cursor.execute(
            "ALTER TABLE items_catalog "
            "MODIFY stock VARCHAR(20) NOT NULL DEFAULT 'pendente'"
        )

    # Bancos criados antes das fotos não têm a coluna `image`.
    cursor.execute(
        "SELECT COUNT(*) FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'items_catalog' "
        "AND COLUMN_NAME = 'image'"
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute("ALTER TABLE items_catalog ADD COLUMN image VARCHAR(255) NULL")

    connection.commit()
    connection.close()


def create_ratings():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ratings (
        rating_id INT AUTO_INCREMENT PRIMARY KEY,
        items_id INT NOT NULL,
        name VARCHAR(100) NOT NULL,
        rating_score DECIMAL(2, 1) NOT NULL,
        FOREIGN KEY (items_id) REFERENCES items_catalog(items_id) ON DELETE CASCADE
    )
    """)
    connection.commit()
    connection.close()