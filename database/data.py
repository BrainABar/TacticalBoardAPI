from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base_query = db_session.query_property()


def init_db():
    import database.models
    Base.metadata.create_all(bind=engine)

