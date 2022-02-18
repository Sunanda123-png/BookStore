from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from urllib.parse import urlparse

# from views import profile
# from views import register


app = Flask(__name__)
# from models import UserModel
from views import *
# app.register_blueprint(profile)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/BookStore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
