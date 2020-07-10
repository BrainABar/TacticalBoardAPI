from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class Reference(Base):
    __tablename__ = 'references'

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    label = Column(String(30), unique=True, nullable=False)
    description = Column(String(140), nullable=True)
    maps = relationship('Map', back_populates='reference', lazy='select')
