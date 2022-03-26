from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    images = db.Column(db.String)
    thread = db.relationship('Thread')
    thread_id = db.Column(db.Integer, db.ForeignKey("thread.id"))

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    is_pinned = db.Column(db.Boolean)
    text = db.Column(db.Text)
    images = db.Column(db.String)
    answers = db.relationship('User')

