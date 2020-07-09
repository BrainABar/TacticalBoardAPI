from pydantic import BaseModel, HttpUrl
from typing import List
from database.schemas.reference import ReferenceSchema

class MapSchema(BaseModel):
    id: int
    label: str
    description: str

    class Config:
        orm_mode = True

'''
class MapReference(MapSchema):
    reference: ReferenceSchema
'''
