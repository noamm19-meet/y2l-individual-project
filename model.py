from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
'''
class Product(Base):
    __tablename__ = 'product'
    '''
class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	fname = Column(String)
	lname = Column(String)
	uname = Column(String)
	password = Column(String)
	email = Column(String)

	def __repr__(self):
		return ("User First Name: {}\n"
				"User Last Year: {} \n"
				"User Name: {} \n"
				"User Password: {} \n"
				"User Email: {}").format(
					self.fname,
					self.lname,
					self.uname,
					self.password,
					self.email)

class Elemnts_modle(Base):
	__tablename__='elemnts'
	Element_id = Column(Integer, primary_key=True)
	uname=Column(String)
	Different=Column(String)
	Time = Column(String)
	Exercise = Column(String)
	Date = Column(String)

	def __repr__(self):
		return ("Element_id: {} \n"
			    "User name: {}\n"
			    "Exercise Name: {} \n"
			    "Different Element: {}\n"
				"Time: {}\n  "			
				"Date: {} \n").format(
					self.Element_id,
					self.uname,
					self.Exercise,
					self.Different,
					self.Time,
					self.Date)
