from flask import Flask
import os

app = Flask("Blog Web App")
app.secret_key = os.environ['SECRET_KEY']

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

from app import models
with app.app_context():
    db.create_all()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

from app.models import User

@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes