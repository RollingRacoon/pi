class Rating:
    def __init__(self, costumer, rating):
        self._costumer = costumer
        self._rating = rating

    def __str__(self):
        return f'{self._costumer}: {self._rating}'