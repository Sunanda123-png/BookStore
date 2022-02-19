from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
from views import *
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/BookStore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
