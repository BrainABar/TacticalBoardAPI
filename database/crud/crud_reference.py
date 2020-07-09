from database.crud.base import CRUDBase, Type
from database.models import Reference


class CRUDreference(CRUDBase[Reference]):
    def __init__(self, model: Type[Reference] = Reference):
        super(CRUDreference, self).__init__(model=model)
