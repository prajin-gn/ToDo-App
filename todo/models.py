from datetime import date
from todo import db

# class User(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=30), nullable=False, unique=True)
#     password = db.Column(db.String(length=60), nullable=False)
#     tasks = db.relationship("Task", backref="owned_user", lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    details = db.Column(db.String(length=150), nullable=False)
    due = db.Column(db.Date())
    priority = db.Column(db.Integer(), default=0 )
    is_complete = db.Column(db.Boolean(), default=False)
    # owner = db.Column(db.Integer(), db.ForeignKey("user.id"))