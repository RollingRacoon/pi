from database.db import connect
from models.rating import Rating

def save(rating_id, rating):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO ratings (rating_id, user_name, rating_score)
        """, (rating_id, rating._user_name, rating._rating_score)
    )
    connection.commit()
    connection.close()

def list_score_by_item(rating_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT user_name, score FROM rating WHERE rating_id = %s", (rating_id)
    )
    lines = cursor.fetchall()
    connection.close()

    rating = []
    for user_name, rating_score in lines:
        rating.append(Rating(user_name, float(rating_score)))
    return rating