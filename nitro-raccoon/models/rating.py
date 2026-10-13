class Rating:
    # Faixa aceita para a nota; a coluna rating_score é DECIMAL(2, 1).
    MIN_SCORE = 0
    MAX_SCORE = 5

    def __init__(self, name, score):
        name = str(name).strip()
        if not name:
            raise ValueError('Informe o nome de quem está avaliando.')

        try:
            score = float(str(score).replace(',', '.'))
        except ValueError:
            raise ValueError('A nota precisa ser um número.') from None

        if not self.MIN_SCORE <= score <= self.MAX_SCORE:
            raise ValueError(
                f'A nota precisa estar entre {self.MIN_SCORE} e {self.MAX_SCORE}.'
            )

        self.name = name
        self.score = round(score, 1)

    def __str__(self):
        return f'{self.name}: {self.score}'