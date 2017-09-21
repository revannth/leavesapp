import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'us-cdbr-iron-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'ba6ad320cb67d2'
app.config['MYSQL_PASSWORD'] = 'd44c8e9f'
app.config['MYSQL_DB'] = 'heroku_fa71028ec71c3a9'
#app.config['MYSQL_DB'] = 'id2597668_vicky'
mysql.init_app(app)
#db = MySQLdb.connect(host='databases.000webhost.com',user='id2597668_saivicky',passwd='chelamela',db='id2597668_vicky')

@app.route('/')
def index():
	return '<h1> Deployed </h1>'

@app.route('/Authenticate')
def Authenticate():

	cursor = mysql.connect.cursor()
	cursor.execute("SELECT* FROM l_available")
	data = cursor.fetchall()
	if data is None :
		return '<h1>Wrong username</h1>'
	else :
		return render_template('index.html',data=data)
	

'''if __name__ == "__main__":
	app.run()
'''
