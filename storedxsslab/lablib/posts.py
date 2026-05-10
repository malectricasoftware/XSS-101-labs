#imports
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os.path import exists
from os import mkdir
from contextlib import contextmanager

#sql alchemy base for tables to inherit from
Base = declarative_base()

# Ensure the directory for the database exists
if not exists("db"):
    mkdir("db")

# Define the Password model
class Post(Base):
    __tablename__ = "Post"
    postid = Column("postid", Integer, primary_key=True)
    author = Column("author", String)
    content = Column("content", String)
    
    def __init__(self, postid, author, content):
        self.postid = postid
        self.author = author
        self.content = content
   

# Database setup
engine = create_engine("sqlite:///db/posts.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

#manage context
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
    finally:
        session.close()

#store credential
def post(author,content):
    with get_session() as session:
        postid=len(session.query(Post).all())
        p = Post(postid,author,content)
        try:
            session.add(p)
            return "Stored post"
        except Exception as e:
            return "Error storing post: {e}"

#load credemtial
def fetch(domain):
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Password).filter(Password.domain == domain).first()

        #if one is found
        if p:
        	return p.ccred

        #error
        else:
            return f"No cred found for '{domain}'"
def fetchall():
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Post).all()
        #if one is found
        if p:
            posts=[{"id":post.postid,"author":post.author,"content":post.content} for post in p[::-1]]
            return posts

        #error
        else:
            return None
#load credential
def update(domain,ccred):
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Password).filter(Password.domain == domain).first()

        #if one is found
        if p:
        	p.ccred=ccred
        	return "updated credential"

        #error
        else:
            return f"No cred found for '{domain}'"
