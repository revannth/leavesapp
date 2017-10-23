#Imports
import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template,redirect,url_for,request,session
from flask_mysqldb import MySQL

#DATABASE CONNECTIONS
app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Revannth@1' 
app.config['MYSQL_DB'] = 'project_dbms' 
mysql.init_app(app)
app.secret_key='revannth this is encryption key'


#ROUTES
@app.route('/')
def index():
	return redirect(url_for('Authenticate'))

@app.route('/home',methods =['POST','GET'])
def home():
	conn=mysql.connect
	cursor = conn.cursor()
	l_applied=[]
	#hash token checking and enabling login
	if 'hashkey' in session and session['hashkey']>0 :
		print session['hashkey'];
		cursor.execute("SELECT ename FROM authorizers INNER JOIN employee ON employee.eid=authorizers.eid AND ename=%s;",username)
		data_auth = cursor.fetchall()
			#print(len(data_auth))
		if len(data_auth)>0:
			type="hod"
		else:
			type="staff"	
	else:
		return '<h1>Your Action will be reported</h1>'
	if request.method =='POST':
		if request.form['submit']=='logout':
			session['hashkey']=-1;
			return redirect(url_for('Authenticate'));
		elif request.form['submit'] == 'show':
			cursor.execute("SELECT ltype,appdate,no_of_days FROM leaves")
			temp_applied = cursor.fetchall()
			l_applied =[list(x) for x in temp_applied]
		elif request.form['submit'] == 'change':
			cursor.execute("UPDATE leaves SET `approveddate`=CURDATE(),`lstatus`='accepted' WHERE eid=10501;")
			print cursor;
			conn.commit()
		elif request.form['submit'] =='apply':
			cursor.execute("insert ")


			print(cursor._executed)

			
	return render_template('home.html',username=username,type=type,l_applied=l_applied)

	

	
@app.route('/Authenticate',methods =['POST','GET'])
def Authenticate():
	error = None
	pos_user = None
	pos_pass = None
	if request.method == 'POST':
		global username
		global password
		global cursor
		global conn
		global eid
		conn=mysql.connect
		cursor = mysql.connect.cursor()
		username = request.form['username']
		password ='('+ 'u'+"'"+ request.form['password'] + "',"+')'
		#print(username)
		
		cursor.execute("SELECT hashkey FROM auth_cont WHERE user=%s",request.form['username'])
		data_user = cursor.fetchall()
		print(data_user)
		#print(username)
		cursor.execute("SELECT hashkey FROM auth_cont WHERE pass=%s",request.form['password'])
		data_pass = cursor.fetchall()

		cursor.execute("SELECT eid FROM employee INNER JOIN auth_cont ON ename=%s;",username)
		eid = cursor.fetchone()
		if data_user==data_pass and data_pass!=() and data_user!=() :
			session['hashkey']=data_user
			return redirect(url_for('home'))
		else :
			error = "Invalid User Name or Password"
	return render_template('login.html',error=error)




if __name__ == "__main__":
	app.run(debug=True)

