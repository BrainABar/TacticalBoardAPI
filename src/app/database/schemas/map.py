from pydantic import BaseModel


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
