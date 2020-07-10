from app import ReferenceSchema
from app import MapSchema
from typing import List

class ReferenceMaps(ReferenceSchema):
    maps: List[MapSchema] = []
