from knowledge_model import Base, Knowledge, Website

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating, host_site_id):
	article_object = Knowledge(
		topic=topic,
		title=title,
		rating=rating,
		host_site_id=host_site_id)
	session.add(article_object)
	session.commit()

def add_site(articles_num, name, rating):
	site_object = Website(
		articles_num=articles_num,
		name=name,
		rating=rating)
	session.add(site_object)
	session.commit()

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles

def query_article_by_topic(topic):
	article = session.query(Knowledge).filter_by(
		topic=topic).first()
	return article

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(title, rating):
	article_object = session.query(
		Knowledge).filter_by(
		title=title).first()
	article_object.rating = rating
	session.commit()

delete_all_articles()

add_article("Computer Science", "Foreign Key", 8, 1)
print(query_article_by_topic("Computer Science").host_site_id)