from database.schemas import ReferenceSchema
from database.schemas import MapSchema
from typing import List

class ReferenceMaps(ReferenceSchema):
    maps: List[MapSchema] = []
