from pydantic import BaseModel


class ReferenceSchema(BaseModel):
    id: int
    label: str
    description: str

    class Config:
        orm_mode = True
