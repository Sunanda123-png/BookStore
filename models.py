from app import db


class UserModel(db.Model):
    __tablename__ = 'registration'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    contact_number = db.Column(db.String(10))
    password = db.Column(db.String(20))
    email_address = db.Column(db.String(30))

    def __init__(self, user_name, first_name, last_name, contact_number, password, email_address):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.contact_number = contact_number
        self.password = password
        self.email_address = email_address

    def __repr__(self):
        return f"{self.user_name}:{self.first_name}:{self.last_name}:{self.contact_number}:{self.password}:{self.email_address}"


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Integer())
    author = db.Column(db.String(80))

    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def json(self):
        return {"name": self.name, "price": self.price, "author": self.author}

