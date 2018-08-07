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
add_article("sam","nothing",3 )
add_article("waseem" , "tennis" , 8)
add_article("shir" , "cs", 10)
add_article("shira", "cycling" , 9.5)
add_article("laith", "sports" , 10000)
add_article("Cristiano Ronaldo" ,"football", 0)
def query_all_articles():
	friend = session.query(
		Knowledge).all()
	return friend

def query_article_by_topic(name):
	article_topic = session.query(
		Knowledge).filter_by(
		name=name).first()
	return article_topic


def delete_article_by_topic(name):
	session.query(Knowledge).filter_by(
		name=name).delete()
	session.commit()

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
	top_five =session.query(Knowledge).order_by(
		Knowledge.rating.desc()).all()
	return top_five[0:6]


edit_article_rating("mor" , 10)
edit_article_rating("waseem", 13)
print(top_five_topics())
#print(query_all_articles())
print (query_article_by_topic("name"))
#print(query_all_articles())
delete_article_by_topic("sam")
delete_all_articles()

