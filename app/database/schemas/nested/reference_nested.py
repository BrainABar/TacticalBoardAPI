from app.database import ReferenceSchema
from app.database import MapSchema
from typing import List

class ReferenceMaps(ReferenceSchema):
    maps: List[MapSchema] = []
