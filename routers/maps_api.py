from database.data import db_session
from database.models.reference import Reference
from database.models.map import Map
from database.models.mapimage import MapImage
from database.models.layer import Layer
from database.schema import ReferenceSchema, MapSchema, ImageSchema, LayerSchema
from sqlalchemy.orm import joinedload
from fastapi import APIRouter
from typing import List

api = APIRouter()


@api.get('/references', response_model=List[ReferenceSchema])
async def get_references():
    ''' List of all references '''
    """
    get:
        summary: References endpoint.
        description: Get a list of all references
        responses:
            200:
                description: Reference objects returned
                schema: ReferenceSchema
            404:
                description: Reference objects not found
    """
    references = db_session.query(Reference).all()
    return references


@api.get('/references/{reference_id}', response_model=ReferenceSchema)
async def get_reference(reference_id: int):
    ''' Get A reference by id '''
    reference = db_session.query(Reference)\
        .options(joinedload(Reference.maps))\
        .filter(Reference.id == reference_id).first()
    return reference


@api.get('/references/{reference_id}/maps', response_model=List[MapSchema])
async def get_maps(reference_id: int):
    ''' List of maps associated with reference id'''
    maps = db_session.query(Map).filter(Reference.id == reference_id).all()
    return maps


@api.get('/maps/{map_id}', response_model=MapSchema)
async def get_map(map_id: int):
    ''' Get map details and list of map urls '''
    map = db_session.query(Map).filter(Map.id == map_id).first()
    return map


@api.get('/maps/{map_id}/images', response_model=List[ImageSchema])
async def get_images(map_id: int):
    ''' Get url list from map id '''
    images = db_session.query(MapImage).filter(Map.id == map_id).all()
    return images


@api.get('/images/{image_id}', response_model=ImageSchema)
async def get_image(image_id: int):
    ''' Get url link and details '''
    image = db_session.query(MapImage).filter(MapImage.id == image_id).first()
    return image


@api.get('/images/{image_id}/layers', response_model=List[LayerSchema])
def get_layers(image_id: int):
    layers = db_session.query(Layer).filter(MapImage.id == image_id).all()
    return layers


@api.get('/layers/<int:layer_id>', response_model=LayerSchema)
async def get_layer(layer_id: int):
    layer = db_session.query(Layer).filter(Layer.id == layer_id).first()
    return layer


'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''