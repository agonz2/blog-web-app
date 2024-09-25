from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)

class Post(db.Model, UserMixin):
    __tablename__ = 'userpost'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    timestamp = db.Column(db.String)
    user_id = db.Column(db.ForeignKey(User.id))