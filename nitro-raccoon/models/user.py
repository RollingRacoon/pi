class User:
    def __init__(self, name, email, hash_password, is_admin=False):
        self.nome = name
        self.email = email
        self._hash_password = hash_password
        self._is_admin = is_admin
        self.id = None

    def __str__(self):
        return f'{self.name} <{self.email}>'

    @property
    def is_admin(self):
        return self._is_admin