from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.database.db import Base

class Reference(Base):
    __tablename__ = 'references'

    label = Column(String(30), unique=True, nullable=False)
    description = Column(String(140), nullable=True)
    maps = relationship('Map', back_populates='reference', lazy='select')
