from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
curr_date = date.today().strftime("%b %d %Y")

with app.app_context():
    db.create_all()


from todo import routes