from app.database.crud.base import CRUDBase, Type
from app.database.models import Map


class CRUDMap(CRUDBase[Map]):
    def __init__(self, model: Type[Map] = Map):
        super(CRUDMap, self).__init__(model=model)
