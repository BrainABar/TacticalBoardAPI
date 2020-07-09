from .session import get_database, engine, Session
from .base_class import Base

def init_database():
    Base.metadata.create_all(bind=engine)