from pydantic import BaseModel, HttpUrl


class LayerSchema(BaseModel):
    id: int
    label: str
    url: HttpUrl

    class Config:
        orm_mode = True