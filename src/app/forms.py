from app import db
from app import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError
import sqlalchemy as sa

class SignUpForm(FlaskForm):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.InputRequired()
    ])
    username = StringField('Username', [
        validators.Length(min=2, max=50), 
        validators.DataRequired(), 
        validators.InputRequired()
    ])
    passwd = PasswordField('Password', [
        validators.Length(min=5, max=50), 
        validators.DataRequired()
    ])
    passwd_confirm = PasswordField('Confirm Password', [
        validators.DataRequired(),
        validators.EqualTo('passwd', message='Passwords must match')
    ])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db.session.query(User).filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')