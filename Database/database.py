# database.py
#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#from sqlalchemy import create_engine
#engine = create_engine('postgresql://avatar:1592@localhost:5432/users')

engine = create_engine('postgresql://avatar:1592@localhost:5432/users', convert_unicode=False)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import models
  Base.metadata.create_all(engine)