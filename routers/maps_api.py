from database.schemas import ReferenceSchema, MapSchema, ImageSchema, LayerSchema
from fastapi import APIRouter
from typing import List
from database.crud import read

api = APIRouter()


@api.get('/references', response_model=List[ReferenceSchema])
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
    return read.get_references()


@api.get('/references/{reference_id}', response_model=ReferenceSchema)
def get_reference(reference_id: int):
    ''' Get A reference by id '''
    return read.get_reference(ref_id=reference_id)


@api.get('/references/{reference_id}/maps', response_model=List[MapSchema])
def get_maps(reference_id: int):
    ''' List of maps associated with reference id'''
    return read.get_maps(ref_id=reference_id)


@api.get('/maps/{map_id}', response_model=MapSchema)
def get_map(map_id: int):
    ''' Get map details and list of map urls '''
    return read.get_map(map_id=map_id)


@api.get('/maps/{map_id}/images', response_model=List[ImageSchema])
def get_images(map_id: int):
    ''' Get url list from map id '''
    return read.get_images(map_id=map_id)


@api.get('/images/{image_id}', response_model=ImageSchema)
def get_image(image_id: int):
    ''' Get url link and details '''
    return read.get_image(image_id=image_id)


@api.get('/images/{image_id}/layers', response_model=List[LayerSchema])
def get_layers(image_id: int):
    return read.get_layers(image_id=image_id)


@api.get('/layers/<int:layer_id>', response_model=LayerSchema)
def get_layer(layer_id: int):
    return read.get_layer(layer_id=layer_id)

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''