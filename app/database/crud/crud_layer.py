from app.database.crud.base import CRUDBase, Type
from app.database.models import Layer


class CRUDLayer(CRUDBase[Layer]):
    def __init__(self, model: Type[Layer] = Layer):
        super(CRUDLayer, self).__init__(model=model)
