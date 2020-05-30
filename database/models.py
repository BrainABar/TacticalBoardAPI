from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .data import Base


class Reference(Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    maps = relationship('Map', back_populates='reference')


class Map(Base):
    __tablename__ = 'map'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    reference_id = Column(Integer, ForeignKey('reference.id'))
    reference = relationship('Reference', back_populates='maps')
