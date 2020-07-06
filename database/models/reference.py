from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database.data import Base
from marshmallow import Schema, fields


class Reference(Base):
    __tablename__ = 'reference'

    id = Column(Integer, primary_key=True)
    label = Column(String)
    description = Column(String)
    maps = relationship('Map', back_populates='reference')


class ReferenceSchema(Schema):
    id = fields.Integer()
    label = fields.String()
    description = fields.String()