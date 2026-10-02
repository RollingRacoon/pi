import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nitro-raccoon"
    )
    return conexao