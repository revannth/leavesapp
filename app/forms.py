#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, Regexp, EqualTo

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[InputRequired(),Length(min=6,max=20),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
	password = PasswordField('Password',validators=[InputRequired(),Length(min=8,max=80)])
	remember_me = BooleanField('Remember Me')

class RegisterForm(FlaskForm):
	email = StringField('Email',validators=[InputRequired(),Email(message="Email Required"),Length(max=50)])
	username = StringField('Username',validators=[InputRequired(),Length(min=6,max=20),Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
	password = PasswordField('Password',validators=[InputRequired(),Length(min=8,max=80),EqualTo('password2',message="Passwords must match")])
	password2 = PasswordField('Confirm Password',validators=[InputRequired])


