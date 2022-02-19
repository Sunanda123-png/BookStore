from flask import request, jsonify
from app import db
from models import UserModel, BookModel
from __main__ import app


@app.route("/", methods=['POST'])
def register():
    """
    This function will take all require fields for user registration
    :return: Status of User Registration
    """
    data = request.get_json()
    user_name = data['user_name']
    first_name = data['first_name']
    last_name = data['last_name']
    contact_number = data['contact_number']
    password = data['password']
    email_address = data['email_address']

    if UserModel.query.filter_by(user_name=user_name).first():
        return jsonify({"message": "Username is already Taken", "data": {"username": user_name}})
    else:
        user = UserModel(user_name, first_name, last_name, contact_number, password, email_address, )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "user is created "})


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user_name = data['user_name']
    password = data['password']
    user = UserModel.query.filter_by(user_name=user_name, password=password).first()
    if user:
        return jsonify({"message": "User Login Successful", "data": {"user_name": user_name}})
    else:
        return jsonify({"message": "provide credential is wrong "})


@app.route("/add", methods=['POST'])
def add_book():
    data = request.get_json()
    name = data['name']
    price = data['price']
    author = data['author']
    if BookModel.query.filter_by(name=name).first():
        return jsonify({"message": "Username is already Taken", "data": {"name": name}})
    else:
        new_book = BookModel(name, price, author)
        db.session.add(new_book)
        db.session.commit()
        return new_book.json(), 201


@app.route("/get", methods=['GET'])
def get_book():
    books = BookModel.query.all()
    return {'Books': list(x.json() for x in books)}


@app.route("/put", methods=['PUT'])
def update_book():
    data = request.get_json()
    name = data['name']
    book = BookModel.query.filter_by(name=name).first()
    if book:
        book.price = data["price"]
        book.author = data["author"]
    else:
        book = BookModel(name=name, **data)

    db.session.add(book)
    db.session.commit()

    return book.json(),200


@app.route("/delete", methods=['DELETE'])
def book_delete():
    data = request.get_json()
    name = data['name']
    book = BookModel.query.filter_by(name=name).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Deleted'}
    else:
        return {'message': 'book not found'}, 404