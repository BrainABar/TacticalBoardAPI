from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class Map(Base):
    __tablename__ = 'map'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    reference_id = Column(Integer, ForeignKey('reference.id'))
    reference = relationship('Reference', back_populates='maps')
    mapImages = relationship('MapImage', back_populates='map', lazy='select')
