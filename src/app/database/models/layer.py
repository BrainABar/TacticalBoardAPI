from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class Layer(Base):
    __tablename__ = 'layers'

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    url = Column(String)
    image_id = Column(UUID(as_uuid=True), ForeignKey('mapImages.id'))
    image = relationship('MapImage', back_populates='layers')
