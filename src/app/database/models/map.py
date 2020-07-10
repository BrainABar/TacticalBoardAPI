from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Map(Base):
    __tablename__ = 'maps'

    label = Column(String)
    description = Column(String)
    reference_id = Column(UUID(as_uuid=True), ForeignKey('references.id'))
    reference = relationship('Reference', back_populates='maps')
    mapImages = relationship('MapImage', back_populates='map', lazy='select')
