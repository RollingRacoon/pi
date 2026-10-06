class Rating:
    def __init__(self, user, rating):
        self._user = user
        self._rating = rating

    def __str__(self):
        return f'{self._user}: {self._rating}'