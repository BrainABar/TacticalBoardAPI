from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class Map(Base):
    __tablename__ = 'maps'

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    label = Column(String)
    description = Column(String)
    reference_id = Column(UUID(as_uuid=True), ForeignKey('references.id'))
    reference = relationship('Reference', back_populates='maps')
    mapImages = relationship('MapImage', back_populates='map', lazy='select')
