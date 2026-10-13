"""
Script de uso único/manual — NUNCA deve virar uma rota pública do Flask.

Uso (a partir da pasta do projeto):
    python scripts/tornar_admin.py email@exemplo.com
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))  # permite `from database.db import connect` rodando de scripts/

from dotenv import load_dotenv
load_dotenv(ROOT.parent / ".env")  # mesmo caminho que o app.py usa
load_dotenv(ROOT / ".env")         # alternativa: .env dentro do projeto

import mysql.connector
from database.db import connect


def tornar_admin(email):
    """Devolve 'feito', 'ja_admin' ou 'nao_encontrado'."""
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT is_admin FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()

        if row is None:
            return 'nao_encontrado'
        if row[0]:
            return 'ja_admin'

        cursor.execute("UPDATE users SET is_admin = TRUE WHERE email = %s", (email,))
        connection.commit()
        return 'feito'
    finally:
        connection.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python scripts/tornar_admin.py email@exemplo.com')
        sys.exit(1)

    email_informado = sys.argv[1].strip()

    try:
        resultado = tornar_admin(email_informado)
    except mysql.connector.Error as error:
        print(f'Erro no banco de dados: {error}')
        sys.exit(1)

    if resultado == 'feito':
        print(f'"{email_informado}" agora é administrador(a).')
    elif resultado == 'ja_admin':
        print(f'"{email_informado}" já era administrador(a).')
    else:
        print(f'Nenhum usuário encontrado com o e-mail "{email_informado}". '
              'A pessoa precisa se cadastrar em /sign_in antes.')
        sys.exit(1)