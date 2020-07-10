from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class MapImage(Base):
    __tablename__ = 'mapImages'
    __table_args__ = (UniqueConstraint('map_id', 'level', name='mapLevel'),)

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    label = Column(String)
    description = Column(String)
    url = Column(String)
    level = Column(Integer)
    map_id = Column(UUID(as_uuid=True), ForeignKey('maps.id'))
    map = relationship('Map', back_populates='mapImages')
    layers = relationship('Layer', back_populates='image', lazy='select')
