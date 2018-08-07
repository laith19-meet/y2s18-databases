from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'friends interests'
	friends_number = Column(Integer,primary_key = True)
	name = Column (String)
	interests= Column( String)

	rating = Column(Integer)

	def __repr__(self):
		return ("friends name: {}\n"
				"friends interests : {}\n"
				"friends rating: {}\n").format(
					self.name,
					self.interests,
					self.rating)




