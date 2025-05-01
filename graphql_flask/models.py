# models.py
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

users_db = [
    User(1, "Alice", "alice@example.com"),
    User(2, "Bob", "bob@example.com"),
]
