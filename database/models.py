from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
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
    __table_args__ = (UniqueConstraint('map_id', 'level', name='mapLevel'),)

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    url = Column(String)
    level = Column(Integer)
    map_id = Column(Integer, ForeignKey('map.id'))
    map = relationship('Map', back_populates='mapImages')
    layers = relationship('Layer', back_populates='image')


class Layer(Base):
    __tablename__ = 'layer'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    url = Column(String)
    image_id = Column(Integer, ForeignKey('mapImage.id'))
    image = relationship('MapImage', back_populates='layers')
