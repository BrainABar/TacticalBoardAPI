from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .data import Base


class Reference(Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    maps = relationship('Map', back_populates='reference')


class Map(Base):
    __tablename__ = 'map'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    reference_id = Column(Integer, ForeignKey('reference.id'))
    reference = relationship('Reference', back_populates='maps')
    mapImages = relationship('MapImage', back_populates='map')


class MapImage(Base):
    __tablename__ = 'mapImage'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    file = Column(String)
    map_id = Column(Integer, ForeignKey('map.id'))
    map = relationship('Map', back_populates='mapImages')
