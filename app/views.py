#views.py
#views.py
from flask import render_template,flash,redirect,url_for,request
from flask_login import login_user,login_required,logout_user,current_user
from app import app,db




@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
	
	return render_template('login.html')



@app.route('/logged_in',methods=['POST'])
def logged_in():
	error=""
	username = request.form['username']
	password = request.form['password']
	employee = Employee.query.filter_by(username=username).first()
	
	if employee is not None and employee.verify_password(password):
		login_user(employee)
		return redirect(url_for('home'))
	else :
		error = " You have either entered the wrong username or the wrong password"
	
	return redirect(url_for('login'))

@app.route('/home',methods=['POST'])
@login_required
def home():
	return render_template('home.html')



