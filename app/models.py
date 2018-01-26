#models.py

from app import db


class Employee(db.Model):
	eid = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(120),unique=True)
	eename = db.Column(db.String(120))
	designation = designation = db.Column(db.String(30))
	department = db.Column(db.String(8))

	def __repr__(self):
		return '<Employee {}{}{}{}{}>'.format(self.eid,self.email,self.eename,self.designation,self.department)


class Authorizers(db.Model):
	eid = db.Column(db.Integer,db.ForeignKey('employee.eid'),primary_key=True)
	department = db.Column(db.String(8))
	designation = db.Column(db.String(30))

	def __repr__(self):
		return '<Authorizers {}{}{}>'.format(self.eid,self.department,self.designation)

class Authorizers_Controller(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(20),unique=True)
	password_hashed = db.Column(db.String(80))




# Leaves Information

class Leaves(db.Model):
	lid = db.Column(db.Integer,primary_key=True)
	appdate = db.Column(db.Date)
	approvedate =  db.Column(db.DateTime)
	eid = db.Column(db.Integer,db.ForeignKey('employee.eid'),primary_key=True)
	lstatus = db.Column(db.String(9)) 
	no_of_days = db.Column(db.Integer)
	rforleave = db.Column(db.String(150))
	rfromhead = db.Column(db.String(150))

	


class L_Available(db.Model):
	eid = db.Column(db.Integer,db.ForeignKey('employee.eid'),primary_key=True)
	ccl = db.Column(db.Integer,default=7)
	cl = db.Column(db.Integer,default=7)
	el = db.Column(db.Integer,default=7)
	eol = db.Column(db.Integer,default=7)
	ml = db.Column(db.Integer,default=7)
	od = db.Column(db.Integer,default=7)







