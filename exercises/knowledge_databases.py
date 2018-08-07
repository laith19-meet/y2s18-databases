from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_article(name , interests, rating ):
	friends_objects = Knowledge(
		name = name,
		interests= interests,
		rating = rating)
	session.add(friends_objects)
	session.commit()
	
add_article ("mor" , "reading " , 9)
add_article("mat" , "math" , 11)
def query_all_articles():
	friend = session.query(
		Knowledge).all()
	return friend
print(query_all_articles())

def query_article_by_topic(name):
	article_topic = session.query(
		Knowledge).filter_by(
		name=name).first()
	return article_topic
print (query_article_by_topic("mor"))


def delete_article_by_topic(name):
	session.query(Knowledge).filter_by(
		name=name).delete()
	session.commit()
delete_article_by_topic("sam")

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(name , rating):
	friends_objects = session.query(
		Knowledge).filter_by(
		name=name).first()
	friends_objects.rating = rating
	session.commit()

def top_five_topics():
	top_five =session.query(Knowledge).filter_by(
		rating=rating).all
	return top_five
print(top_five_topics())
edit_article_rating("mor" , 10)
print(query_all_articles())
delete_all_articles()

