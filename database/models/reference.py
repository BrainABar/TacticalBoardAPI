from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.data import Base


class Reference(Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    maps = relationship('Map', back_populates='reference', lazy='select')
