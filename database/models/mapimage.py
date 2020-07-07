from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database.data import Base

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
    layers = relationship('Layer', back_populates='image', lazy='dynamic')
