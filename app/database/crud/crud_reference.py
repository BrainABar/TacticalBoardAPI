from src.app import CRUDBase, Type
from src.app import Reference


class CRUDreference(CRUDBase[Reference]):
    def __init__(self, model: Type[Reference] = Reference):
        super(CRUDreference, self).__init__(model=model)
