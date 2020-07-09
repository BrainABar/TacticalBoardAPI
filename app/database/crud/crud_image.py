from app.database.crud.base import CRUDBase, Type
from app.database.models import MapImage


class CRUDImage(CRUDBase[MapImage]):
    def __init__(self, model: Type[MapImage] = MapImage):
        super(CRUDImage, self).__init__(model=model)
