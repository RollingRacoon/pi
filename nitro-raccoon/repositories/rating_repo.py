# Repositório de avaliações: grava e lê as notas dos itens.
from database.db import connect


def save(items_id, rating):
    # Grava uma avaliação (já validada pela classe Rating) ligada a um item.
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO ratings (items_id, name, rating_score) VALUES (%s, %s, %s)",
            (items_id, rating.name, rating.score),
        )
        connection.commit()
    finally:
        connection.close()


def list_score_by_item(items_id):
    # Import feito aqui dentro, e não no topo do arquivo.
    from models.rating import Rating

    connection = connect()
    try:
        cursor = connection.cursor()
        # Mais recentes primeiro.
        cursor.execute(
            "SELECT name, rating_score FROM ratings WHERE items_id = %s ORDER BY rating_id DESC",
            (items_id,),
        )
        lines = cursor.fetchall()
    finally:
        connection.close()

    # O banco devolve Decimal; converte para float e recria os objetos Rating.
    return [Rating(name, float(score)) for name, score in lines]