import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template,redirect,url_for,request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'ba6ad320cb67d2'
app.config['MYSQL_PASSWORD'] = 'd44c8e9f'
app.config['MYSQL_DB'] = 'heroku_fa71028ec71c3a9' 

'''app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Revannth@1'
app.config['MYSQL_DB'] = 'auth_cont' 
'''

#app.config['MYSQL_DB'] = 'id2597668_vicky'
mysql.init_app(app)
#db = MySQLdb.connect(host='databases.000webhost.com',user='id2597668_saivicky',passwd='chelamela',db='id2597668_vicky')

@app.route('/')
def index():
	return '<h1> Deployed </h1>'

@app.route('/Authenticate',methods =['GET','POST'])
def Authenticate():
	error = None
	username = request.form['username']
	password = request.form['password']
	cursor = mysql.connect.cursor()
	cursor.execute("SELECT user FROM auth_cont")
	data_user = cursor.fetchall()
	cursor.execute("SELECT pass FROM auth_cont")
	data_pass = cursor.fetchall()
	if request.method == 'POST':
		for key,value in enumerate(data_user):
			if value == username:
				pos_user = key
		for key,value in enumerate(data_pass):
			if value == password:
				pos_pass = key

	if pos_user == pos_pass:
		return redirect(url_for('index'))
	else:
		error = "Invalid User Name or Password"
	return render_template('login.html',error=error)

if __name__ == "__main__":
	app.run()

