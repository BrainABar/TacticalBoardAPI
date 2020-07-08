from pydantic import BaseModel


class ReferenceSchema(BaseModel):
    id: int
    label: str
    description: str

    #maps = fields.Nested(lambda: MapSchema, many=True, only=("id", "label", ))
    class Config:
        orm_mode = True