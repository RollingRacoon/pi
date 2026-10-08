from database.db import connect
from models.rating import Rating

def save(rating_id, rating):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO ratings (rating_id, name, rating_score)
        """, (rating_id, rating._name, rating._rating_score)
    )
    connection.commit()
    connection.close()

def list_score_by_item(rating_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT name, score FROM rating WHERE rating_id = %s", (rating_id)
    )
    lines = cursor.fetchall()
    connection.close()

    rating = []
    for name, rating_score in lines:
        rating.append(Rating(name, float(rating_score)))
    return rating