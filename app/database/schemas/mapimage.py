from pydantic import BaseModel, HttpUrl


class ImageSchema(BaseModel):
    id: int
    label: str
    url: HttpUrl
    description: str
    level: int

    class Config:
        orm_mode = True
