from database.db import connect
from models.user import User


def create_users():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            hash_password VARCHAR(255) NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE 
        )
    """)
    connection.commit()
    connection.close()

def save(user):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO users (name, email, hash_password)
        VALUES (%s, %s, %s)
        """, (user.name, user.email, user._hash_password)
    )
    connection.commit()
    generated_id = cursor.lastrowid
    connection.close()

    user.id = generated_id
    return generated_id

def seek_by_email(email):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT user_id, name, email, hash_password, is_admin FROM users WHERE email = %s", (email,)
    )
    line = cursor.fetchone()
    connection.close()

    if line is None:
        return None

    user_id, name, email, hash_password, is_admin = line
    user = User(name, email, hash_password, is_admin=bool(is_admin))
    user.id = user_id
    return user

def seek_by_id(user_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT user_id, name, email, hash_password, is_admin FROM users WHERE user_id = %s", (user_id,)
    )
    line = cursor.fetchone()
    connection.close()

    if line is None:
        return None
    user_id, name, email, hash_password, is_admin = line
    user = User(name, email, hash_password, is_admin=bool(is_admin))
    user.id = user_id
    return user

def list_all():
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT user_id, name, email, hash_password, is_admin FROM users ORDER BY name"
        )
        rows = cursor.fetchall()
    finally:
        connection.close()

    users = []
    for user_id, name, email, hash_password, is_admin in rows:
        user = User(name, email, hash_password, is_admin=bool(is_admin))
        user.id = user_id
        users.append(user)
    return users


def set_admin(user_id, value):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE users SET is_admin = %s WHERE user_id = %s", (bool(value), user_id)
        )
        connection.commit()
    finally:
        connection.close()