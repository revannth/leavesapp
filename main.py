import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,request 
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'databases.000webhost.com'
app.config['MYSQL_USER'] = 'id2597668_saivicky'
app.config['MYSQL_PASSWORD'] = 'chelamela'
app.config['MYSQL_DB'] = 'id2597668_vicky'
mysql.init_app(app)

@app.route('/')
def index():
	return '<h1> Deployed </h1>'

@app.route('/Authenticate')
def Authenticate():
	username = request.args.get('Username')
	password = request.args.get('Password')
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT* FROM l_available")
	data = cursor.fetchone()
	if data is None :
		return "Wrong username"
	else :
		return data

