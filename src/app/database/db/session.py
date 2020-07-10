from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 'db' is the name mapped by docker based on the dockerfile. Must run on the same network. Otherwise use 'localhost'
engine = create_engine('postgresql://postgres:postgres@db:5432/postgres', echo=True)
session_factory = sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine)
Session = scoped_session(session_factory=session_factory)


def get_database():
    db = Session()
    try:
        yield db
    finally:
        Session.remove()
