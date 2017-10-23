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


#ROUTES-These are the pythonic notations to link a url with a python function
@app.route('/')
def index():
	return redirect(url_for('Authenticate'))




#Dashboard
@app.route('/home',methods =['POST','GET'])
def home():


	#Creating a connection object to commit changes
	conn=mysql.connect
	cursor = conn.cursor()
	l_applied=[]


	#hash token checking and enabling login
	if 'hashkey' in session and session['hashkey']>0 :
		print session['hashkey'];
		cursor.execute("SELECT ename FROM authorizers INNER JOIN employee ON employee.eid=authorizers.eid AND ename=%s;",username)
		data_auth = cursor.fetchall()
			#print(len(data_auth))

	#The staff or HOD is directed to their respective page		
		if len(data_auth)>0:
			type="hod"
		else:
			type="staff"	

	#If session is hijacked then this page is displayed		
	else:
		return '<h1>Your Action will be reported</h1>'

	#Once the user enters any post menthod we enter into this segment of the code
	if request.method =='POST':

	#Logout
		if request.form['submit']=='logout':
			session['hashkey']=-1;
			return redirect(url_for('Authenticate'));

	#According to the user logged in, we take the leaves information and store them in a variable
		elif request.form['submit'] == 'show':
			cursor.execute("SELECT eid,ename,ltype,appdate,no_of_days FROM leaves natural JOIN employee WHERE lstatus='applied' ")
			temp_applied = cursor.fetchall()
			l_applied =[list(x) for x in temp_applied]
			print(l_applied)

	#Leave Approval query
		elif request.form['submit']=='change':
			cursor.execute("UPDATE leaves SET `approveddate`=CURDATE(),`lstatus`='accepted' WHERE eid="+str(request.form['eid']))
			conn.commit()

	#Leave Rejection query
		elif request.form['submit'] =='reject':
			cursor.execute("UPDATE leaves SET `lstatus`='rejected' WHERE eid=+str(request.form['eid']")


	#Leave apply query
		elif request.form['submit'] =='apply':
			#print("insert into leaves(`eid`,`ltype`,`rforleave`,`appdate`,`no_of_days`) values("+str(eid[0])+",'"+request.form['leave']+"','"+ request.form['reason']+"','"+request.form['date']+"',"+str(request.form['days'])+")");
			cursor.execute("insert into leaves(`eid`,`ltype`,`rforleave`,`appdate`,`no_of_days`) values('"+str(eid[0]).strip('[]')+"','"+request.form['leave']+"','"+ request.form['reason']+"','"+request.form['date']+"',"+str(request.form['days'])+")");
			#cursor.execute("insert into leaves(`eid`,`ltype`,`no_of_days`) values(10507,'c_l',4)")
			conn.commit()
			print(cursor._executed)


		
			
	#Returning a HTML template	
	return render_template('home.html',username=username,type=type,l_applied=l_applied)



	

#Login Page
@app.route('/Authenticate',methods =['POST','GET'])
def Authenticate():

#Some variables that we will be using throughout the application
	error = None
	pos_user = None
	pos_pass = None

#If POST method is called from the server
	if request.method == 'POST':
		global username
		global password
		global cursor
		global conn
		global eid


#Taking the password and username from the user to validate in the later section
		conn=mysql.connect
		cursor = mysql.connect.cursor()
		username = request.form['username']
		password ='('+ 'u'+"'"+ request.form['password'] + "',"+')'
		#print(username)

#Taking the Hashkeys
		cursor.execute("SELECT hashkey FROM auth_cont WHERE user=%s",request.form['username'])
		data_user = cursor.fetchall()
		print(data_user)
		#print(username)
		cursor.execute("SELECT hashkey FROM auth_cont WHERE pass=%s",request.form['password'])
		data_pass = cursor.fetchall()


#Validating the user name and password	
		cursor.execute("SELECT eid FROM employee INNER JOIN auth_cont ON ename=%s;",username)
		eid_applied = cursor.fetchall()
		eid  =[list(x) for x in eid_applied]
		if data_user==data_pass and data_pass!=() and data_user!=() :
			session['hashkey']=data_user
			return redirect(url_for('home'))
		else :
			error = "Invalid User Name or Password"
	return render_template('login.html',error=error)







#This is included whenever the app is run on a local server, identicating main as the localserver
if __name__ == "__main__":
	app.run(debug=True)