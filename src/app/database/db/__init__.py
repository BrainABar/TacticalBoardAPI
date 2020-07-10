from .session import get_database, engine, Session
from .base_class import Base

def init_database():
    from app.database import models
    Base.metadata.create_all(bind=engine)
