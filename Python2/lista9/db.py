import sys
from random import sample, randint
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, validates

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

	def ppl(self):
		return [1 for p in self.people]

	def __repr__(self):
		return f"Film(id={self.id}, title={self.title}, date={self.date}, people={self.people})"


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///:memory:', echo=False)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()





''' Simple API '''
#########################################################

def get(table):
	return session.query(table).all()

def getAll():
	return get(Film) + get(Person)
   
def getId(table, id):
    return session.query(table).get(id)

def push(object):
	session.add(object)
	session.commit()

def log(*tokens):
	for t in tokens:
		if isinstance(t, list): log(*t)
		else: print('\033[93m' + str(t))

def err(msg):
	print('\033[91m' + str(msg))

def classify(classname):
	try: return getattr(sys.modules[__name__], classname)
	except: log(classname, "table does not exist")


#########################################################
''' Generate some data and run database'''

NAMES = '''
Michael
Christopher
Jessica
Matthew
Ashley
Jennifer
Joshua
Amanda
Daniel
David
James
Robert
John
Joseph
Andrew
Ryan
Brandon
Jason
Justin
Sarah
William
Jonathan
Stephanie
Brian
Nicole
Nicholas
Anthony
Heather
Eric
Elizabeth
Adam
Megan
Melissa
Kevin
Steven
Thomas
Timothy
Christina
Kyle
Rachel
Laura
Lauren
Amber
Brittany
Danielle
Richard
Kimberly
Jeffrey
Amy
Crystal
Michelle
Tiffany
Jeremy
Benjamin
Mark
Emily
Aaron
Charles
Rebecca
Jacob
Stephen
Patrick
Sean
Erin
Zachary
Jamie
Kelly
Samantha
Nathan
Sara
Dustin
Paul
Angela
Tyler
Scott
Katherine
Andrea
Gregory
'''.split('\n')


SURNAMES = '''
SMITH
JOHNSON
WILLIAMS
JONES
BROWN
DAVIS
MILLER
WILSON
MOORE
TAYLOR
ANDERSON
THOMAS
JACKSON
WHITE
HARRIS
MARTIN
THOMPSON
GARCIA
MARTINEZ
ROBINSON
CLARK
RODRIGUEZ
LEWIS
LEE
WALKER
HALL
ALLEN
YOUNG
HERNANDEZ
KING
WRIGHT
LOPEZ
HILL
SCOTT
GREEN
ADAMS
BAKER
GONZALEZ
NELSON
CARTER
MITCHELL
PEREZ
ROBERTS
TURNER
PHILLIPS
CAMPBELL
PARKER
EVANS
EDWARDS
COLLINS
STEWART
SANCHEZ
MORRIS
ROGERS
REED
'''.lower().split('\n')


MOVIES ='''The Godfather
The Dark Knight
Pulp Fiction
The Lord of the Rings: The Return of the King
Forrest Gump
Inception
The Matrix
Star Wars
Interstellar
Whiplash
Gladiator
'''.split('\n')


from random import choice
PEOPLE = [ Person(name = choice(NAMES) + " " + choice(SURNAMES)) for _ in range(10) ]
FILMS = [Film(title = movie, people = sample(PEOPLE, randint(0,3))) for movie in MOVIES]

session.add_all(PEOPLE + FILMS)
session.commit()