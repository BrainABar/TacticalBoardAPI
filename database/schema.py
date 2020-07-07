from pydantic import BaseModel, HttpUrl
from typing import List


class LayerSchema(BaseModel):
    id: int
    label: str
    url: HttpUrl

    class Config:
        orm_mode = True


class ImageSchema(BaseModel):
    id: int
    label: str
    url: HttpUrl
    description: str
    level: int

    class Config:
        orm_mode = True


class MapSchema(BaseModel):
    id: int
    label: str
    description: str

    #reference = fields.Nested(lambda: ReferenceSchema, only=("id", "label",))
    class Config:
        orm_mode = True


class ReferenceSchema(BaseModel):
    id: int
    label: str
    description: str

    #maps = fields.Nested(lambda: MapSchema, many=True, only=("id", "label", ))
    class Config:
        orm_mode = True