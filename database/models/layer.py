from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Layer(Base):
    __tablename__ = 'layer'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    url = Column(String)
    image_id = Column(Integer, ForeignKey('mapImage.id'))
    image = relationship('MapImage', back_populates='layers')
