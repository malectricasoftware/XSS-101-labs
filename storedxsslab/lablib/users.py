#imports
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os.path import exists
from os import mkdir
from contextlib import contextmanager
from hashlib import sha1

Base = declarative_base()


if not exists("db"):
    mkdir("db")


class User(Base):
    __tablename__ = "User"
    name = Column("name", String, primary_key=True)
    phash = Column("phash", String)

    
    def __init__(self, name, phash):
        self.name = name
        self.phash = phash

# Database setup
engine = create_engine("sqlite:///db/users.db")
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
def create(name,password):
    with get_session() as session:
        u = User(name,sha1(password.encode("utf-8")).hexdigest())
        try:
            session.add(u)
            return True
        except:
            return False

#load credemtial
def login(name,password):

    with get_session() as session:

        u = session.query(User).filter(User.name==name,User.phash==sha1(password.encode("utf-8")).hexdigest()).first()

        if u:
        	return True

        else:
            return False

