from database.schemas import MapSchema, ImageSchema, LayerSchema
from database import schemas
from database.schemas import nested
from fastapi import APIRouter
from typing import List
from database import crud
from database.crud import read

api = APIRouter()


@api.get('/references', response_model=List[schemas.ReferenceSchema])
def get_references():
    '''
    get:
        summary: References endpoint.
        description: Get a list of all references
        responses:
            200:
                description: Reference objects returned
                schema: ReferenceSchema
            404:
                description: Reference objects not found
    '''
    return crud.reference.get_multiple()


@api.get('/references/{reference_id}', response_model=schemas.ReferenceSchema)
def get_reference(reference_id: int):
    ''' Get A reference by id '''
    return crud.reference.get(model_id=reference_id)


@api.get('/references/{reference_id}/maps', response_model=nested.ReferenceMaps)
def get_maps(reference_id: int):
    ''' List of maps associated with reference id'''
    return crud.reference.get_relationships(model_id=reference_id)


@api.get('/maps/{map_id}', response_model=schemas.MapSchema)
def get_map(map_id: int):
    ''' Get map details and list of map urls '''
    return crud.map.get(model_id=map_id)


@api.get('/maps/{map_id}/images')
def get_images(map_id: int):
    ''' Get url list from map id '''
    return crud.map.get_relationships(model_id=map_id)


@api.get('/images/{image_id}')
def get_image(image_id: int):
    ''' Get url link and details '''
    return crud.image.get(model_id=image_id)


@api.get('/images/{image_id}/layers')
def get_layers(image_id: int):
    return crud.image.get_relationships(model_id=image_id)


@api.get('/layers/<int:layer_id>')
def get_layer(layer_id: int):
    return crud.layer.get(model_id=layer_id)

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''