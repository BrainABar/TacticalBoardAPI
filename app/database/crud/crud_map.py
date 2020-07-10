from src.app import CRUDBase, Type
from src.app import Map


class CRUDMap(CRUDBase[Map]):
    def __init__(self, model: Type[Map] = Map):
        super(CRUDMap, self).__init__(model=model)
