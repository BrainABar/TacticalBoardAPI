from src.app import CRUDBase, Type
from src.app import MapImage


class CRUDImage(CRUDBase[MapImage]):
    def __init__(self, model: Type[MapImage] = MapImage):
        super(CRUDImage, self).__init__(model=model)
