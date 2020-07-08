from pydantic import BaseModel, HttpUrl
from typing import List


class MapSchema(BaseModel):
    id: int
    label: str
    description: str

    #reference = fields.Nested(lambda: ReferenceSchema, only=("id", "label",))
    class Config:
        orm_mode = True
