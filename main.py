import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template,redirect,url_for,request,session
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
app.secret_key='revannth this is encryption key'
#db = MySQLdb.connect(host='databases.000webhost.com',user='id2597668_saivicky',passwd='chelamela',db='id2597668_vicky')

@app.route('/')
def index():
	return redirect(url_for('Authenticate'))
@app.route('/home')
def home():

	if 'hashkey' in session and session['hashkey']>0 :
		cursor = mysql.connect.cursor()
		cursor.execute("SELECT ename FROM authorizers WHERE ename=%s",username)
		data_auth = cursor.fetchall()
		if data_auth != None:
			return render_template('home_hod.html',username=username)
		else :
			return render_template('home.html',username=username)
	else :
		return '<h1>Your Action will be reported</h1>'

	
@app.route('/Authenticate',methods =['POST','GET'])
def Authenticate():
	error = None
	pos_user = None
	pos_pass = None
	if request.method == 'POST':
		username = request.form['username']
		global username
		password ='('+ 'u'+"'"+ request.form['password'] + "',"+')'
		global password
		#print(username)
		cursor = mysql.connect.cursor()
		cursor.execute("SELECT hashkey FROM auth_cont WHERE user=%s",request.form['username'])
		data_user = cursor.fetchall()
		print(data_user)
		#print(username)
		cursor.execute("SELECT hashkey FROM auth_cont WHERE pass=%s",request.form['password'])
		data_pass = cursor.fetchall()
		#if request.method == 'POST':
		'''for key,value in enumerate(data_user):
			if value == username:
				pos_user = key
		for key,value in enumerate(data_pass):
			if value == password:
				pos_pass = key
		if pos_user == pos_pass:
			return redirect(url_for('home'))
		else:
			error = "Invalid User Name or Password"  '''
		if data_user==data_pass and data_pass!=() and data_user!=() :
			session['hashkey']=data_user
			return redirect(url_for('home'))
		else :
			error = "Invalid User Name or Password"
	return render_template('login.html',error=error)

if __name__ == "__main__":
	app.run(debug=True)

