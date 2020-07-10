from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Layer(Base):
    __tablename__ = 'layers'

    url = Column(String)
    image_id = Column(UUID(as_uuid=True), ForeignKey('mapImages.id'))
    image = relationship('MapImage', back_populates='layers')
