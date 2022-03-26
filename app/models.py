from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

#threads_users = db.Table('threads_users',db.Column("thread_id", db.Integer, db.ForeignKey("thread.id")),db.Column("user_id", db.Integer, db.ForeignKey("user.id")))

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

