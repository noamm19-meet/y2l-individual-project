from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def Login(fname, lname ,uname , password ):
	"""
	Add a student to the database, given
	their name, year, and whether they have127.0.0.1:5000
	finished the lab.
	"""
	user_object = User(
		fname=fname,
		lname=lname,
		uname=uname,
		password=password)
	session.add(user_object)
	session.commit()

def Register(fname, lname ,uname , password ):
	"""
	Add a student to the database, given
	their name, year, and whether they have127.0.0.1:5000
	finished the lab.
	"""
	user_object = User(
		fname=fname,
		lname=lname,
		uname=uname,
		password=password)
	session.add(user_object)
	session.commit()


def query_by_name(uname):
	"""
	Find the first student in the database,
	by their name
	"""
	user = session.query(User).filter_by(
		uname=uname).first()
	return user

def query_all():
	"""
	Print all the students in the database.
	"""
	users = session.query(User).all()
	return users

def delete_User(uname):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(User).filter_by(
		uname=uname).delete()
	session.commit()

def update_password(uname, password):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	user_object = session.query(User).filter_by(
		uname=uname).first()
	user_object.password = password
	session.commit()

def query_by_id(user_id):
    user = session.query(User).filter_by(
        user_id=user_id).first()
    return user

def add_session( Different , Element , uname , Date , Time):
	Session_object = Elemnts_modle(
		uname=uname,
		Different=Different,
		Element=Element,
		Date = Date,
		Time = Time)
	session.add(post_object)
	session.commit()

def  query_session_by_user(uname):
	 user = session.query(User).filter_by(
        uname=uname).all()

