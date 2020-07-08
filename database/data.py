from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
session_factory = sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)
Session = scoped_session(session_factory=session_factory)
Base = declarative_base()

def init_database():
    import database.models
    Base.metadata.create_all(bind=engine)


def get_database():
    db = Session()
    try:
        yield db
    finally:
        Session.remove()
