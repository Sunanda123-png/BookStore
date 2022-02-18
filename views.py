from flask import request, jsonify
from app import db
from models import UserModel
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
        user = UserModel(user_name, first_name, last_name,contact_number,password, email_address, )
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
        return jsonify({"message": "User Login Successful", "data":{"user_name":user_name}})
    else:
        return jsonify({"message":"provide credential is wrong "})
