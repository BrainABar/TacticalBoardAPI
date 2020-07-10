from sqlalchemy import Column, TIMESTAMP, String, text
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import time

@as_declarative()
class Base(object):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    last_updated = Column(TIMESTAMP, onupdate=time.time(), server_default=text('CURRENT_TIMESTAMP'))
    __name__ = Column(String)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
