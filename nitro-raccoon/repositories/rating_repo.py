from database.db import connect


def save(items_id, rating):
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
    from models.rating import Rating

    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name, rating_score FROM ratings WHERE items_id = %s ORDER BY rating_id DESC",
            (items_id,),
        )
        lines = cursor.fetchall()
    finally:
        connection.close()

    return [Rating(name, float(score)) for name, score in lines]