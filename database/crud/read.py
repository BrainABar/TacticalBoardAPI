from database.data import get_database
from sqlalchemy.orm import joinedload
from database.models.reference import Reference
from sqlalchemy.orm import Session
from database.models.reference import Reference
from database.models.map import Map
from database.models.mapimage import MapImage
from database.models.layer import Layer


def get_references(db: Session = next(get_database())):
    references = db.query(Reference).all()
    return references


def get_reference(ref_id: int, db: Session = next(get_database())):
    reference = db.query(Reference)\
        .options(joinedload(Reference.maps))\
        .filter(Reference.id == ref_id).first()
    return reference


def get_maps(ref_id: int, db: Session = next(get_database())):
    maps = db.query(Map).filter(Reference.id == ref_id).all()
    return maps


def get_map(map_id: int, db: Session = next(get_database())):
    map = db.query(Map).filter(Map.id == map_id).first()
    return map


def get_images(map_id: int, db: Session = next(get_database())):
    images = db.query(MapImage).filter(Map.id == map_id).all()
    return images


def get_image(image_id: int, db: Session = next(get_database())):
    image = db.query(MapImage).filter(MapImage.id == image_id).first()
    return image


def get_layers(image_id: int, db: Session = next(get_database())):
    layers = db.query(Layer).filter(MapImage.id == image_id).all()


def get_layer(layer_id: int, db: Session = next(get_database())):
    layer = db.query(Layer).filter(Layer.id == layer_id).first()
    return layer