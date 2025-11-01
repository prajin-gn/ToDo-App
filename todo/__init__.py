from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)
curr_date = date.today().strftime("%b %d %Y")

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    details = db.Column(db.String(length=150), nullable=False)
    due = db.Column(db.Date())
    priority = db.Column(db.String(length=10), default=0 )
    is_complete = db.Column(db.Boolean(), default=False)

with app.app_context():
    db.create_all()


from todo import routes