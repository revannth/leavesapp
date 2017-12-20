#views.py

from flask import Flask,render_template,flash,redirect,url_for
from flask_user import login_required
from app import app
from . forms import LoginForm,RegisterForm
from . models import User

@app.route('/')
def index():
	return redirect(url_for('login'))


#Login Page
@app.route('/login',methods =['POST','GET'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				return redirect(url_for('dashboard'))
		return '<h1> Ivalid Username or Password</h1>'q
		

	return render_template('login.html',form=form)

@app.route('/register',methods=['POST','GET'])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		new_user = User(username=form.username.data,email=form.email.data,password=form.password.data)
		db.session.add(new_user)
		db.session.commit()


	return render_template('register.html',form=form)




