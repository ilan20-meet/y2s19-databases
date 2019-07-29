from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'articles'
	article_num = Column(Integer, primary_key=True)
	topic = Column(String)
	title = Column(String)
	rating = Column(Integer)

	host_site = relationship("Website")
	host_site_id = Column(Integer, ForeignKey("website.site_id"))
class Website(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ = 'website'
	site_id = Column(Integer, primary_key=True)
	articles_num = Column(Integer)
	name = Column(String)
	rating = Column(Integer)