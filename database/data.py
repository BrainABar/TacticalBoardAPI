from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
default_session = sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)
Session = scoped_session(default_session)
Base = declarative_base()
Base.query = Session.query_property()


def init_database():
    import database.models
    Base.metadata.create_all(bind=engine)


def get_database():
    db = Session()
    try:
        yield db
    finally:
        db.close()
