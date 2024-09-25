from app import app, db
from app.models import User
from app.forms import SignUpForm, LoginForm
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        loggedUser = db.session.query(User).filter_by(username = form.username.data).first()
        if loggedUser and bcrypt.checkpw(form.passwd.data.encode('utf-8'), loggedUser.passwd):
            login_user(loggedUser, remember=form.remember_me.data)
            return redirect(url_for('home'))
        elif not loggedUser:
            return redirect(url_for('signup'))
        
    return render_template('index.html', form=form)

@app.route('/accounts/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.passwd.data == form.passwd_confirm.data:
            hashed_password = bcrypt.hashpw(form.passwd.data.encode('utf-8'), bcrypt.gensalt())
            user_obj = User(name=form.name.data, username=form.username.data, passwd=hashed_password)
            user = form.username.data
            first_name = form.name.data
            print(f"{first_name} successfully created an account: {user}")
            db.session.add(user_obj)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('auth/signup.html', form=form)

@app.route('/home')
def home():
    return render_template('blog/home.html')

@app.route('/user/signout', methods=['GET', 'POST'])
def signout():
    print("was called")
    if current_user.is_authenticated:
        print("is logged in")
        logout_user()
        print("logged user out")
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def list_users():
    pass