#import pymysql
#pymysql.install_as_MySQLdb()
from flask import Flask,render_template
#import MySQLdb

app = Flask(__name__)
#mysql = MySQL(app)
#app.config['MYSQL_HOST'] = 'databases.000webhost.com'
#app.config['MYSQL_USER'] = 'id2597668_saivicky'
#app.config['MYSQL_PASSWORD'] = 'chelamela'
#app.config['MYSQL_DB'] = 'id2597668_vicky'
#mysql.init_app(app)
#db = MySQLdb.connect(host='databases.000webhost.com',user='id2597668_saivicky',passwd='chelamela',db='id2597668_vicky')

@app.route('/')
def index():
	return '<h1> Deployed </h1>'

"""@app.route('/Authenticate')
def Authenticate():
	cursor = db.cursor()
	cursor.execute("SELECT* FROM l_available")
	data = cursor.fetchall()
	if data is None :
		return '<h1>Wrong username</h1>'
	else :
		return render_template('index.html')
"""	

#if __name__ == "__main__":
#   app.run()

