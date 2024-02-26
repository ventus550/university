import sys
from random import sample, randint
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from sqlalchemy.sql.base import PARSE_AUTOCOMMIT

Base = declarative_base()

class Person(Base):
	__tablename__ = 'Person'
	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)
	film = Column(Integer, ForeignKey('Film.id'))
	
	def __repr__(self):
		return f"Person(id={self.id}, name={self.name}, film={self.film})"


class Film(Base):
	__tablename__ = 'Film'
	id = Column(Integer, primary_key=True)
	title = Column(String(30), nullable=False)
	date = Column(DateTime,default=datetime.datetime.utcnow)
	people = relationship('Person')

	def __repr__(self):
		return f"Film(id={self.id}, name={self.title}, film={self.date}, people={self.people})"


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()





''' Simple API '''
#########################################################

def get(table):
	return session.query(table).all()
     
def getId(table, id):
    return session.query(table).get(id)

def push(object):
	session.add(object)
	session.commit()

def log(*tokens):
	for t in tokens:
		if isinstance(t, list): log(*t)
		else: print('\033[93m' + str(t))

def classify(classname):
	try: return getattr(sys.modules[__name__], classname)
	except: log(classname, "table does not exist")


#########################################################
''' Generate some data and run parser '''

from argparse import ArgumentParser

def command():

	TABLE = 'table'
	WRITE = 'wypisz'
	ADD   = 'dodaj'
	NAME  = 'imie'

	parser = ArgumentParser()
	parser.add_argument(TABLE)
	parser.add_argument('--' + WRITE, action='store_true')
	parser.add_argument('--' + ADD, action='store_true')
	parser.add_argument('--' + NAME)

	tokens = vars(parser.parse_args())
	print(tokens)

	if tokens[WRITE]:
		log(get(classify(tokens[TABLE])))

	elif tokens[ADD]:
		cls = classify(tokens[TABLE])
		if cls == Person:
			push(Person(name=tokens[NAME]))
			log(get(Person))

		else:
			log("Bad command")

	else:
		log("No action specified")




PEOPLE = [ Person(name=name) for name in 'ABCDEFGHIJKLMNOPERSTQ' ]
FILMS = [Film(title = f"MOVIE{i}", people = sample(PEOPLE, randint(0,3))) for i in range(10)]

session.add_all(PEOPLE + FILMS)
session.commit()

command()