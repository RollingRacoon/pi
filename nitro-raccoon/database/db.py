import mysql.connector

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nitro-raccoon"
    )
    return connection