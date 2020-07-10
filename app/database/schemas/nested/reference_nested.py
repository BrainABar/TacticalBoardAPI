from src.app import ReferenceSchema
from src.app import MapSchema
from typing import List

class ReferenceMaps(ReferenceSchema):
    maps: List[MapSchema] = []
