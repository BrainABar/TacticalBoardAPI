from fastapi import APIRouter
from app.database import crud
from sqlalchemy.dialects.postgresql import UUID

api = APIRouter()


@api.get('/references')
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


@api.get('/references/{reference_id}')
def get_reference(reference_id: str):
    ''' Get A reference by id '''
    return crud.reference.get(model_id=reference_id)


@api.get('/references/{reference_id}/maps')
def get_maps(reference_id: str):
    ''' List of maps associated with reference id'''
    return crud.reference.get_relationships(model_id=reference_id)


@api.get('/maps/{map_id}')
def get_map(map_id: str):
    ''' Get map details and list of map urls '''
    return crud.map.get(model_id=map_id)


@api.get('/maps/{map_id}/images')
def get_images(map_id: str):
    ''' Get url list from map id '''
    return crud.map.get_relationships(model_id=map_id)


@api.get('/images/{image_id}')
def get_image(image_id: str):
    ''' Get url link and details '''
    return crud.image.get(model_id=image_id)


@api.get('/images/{image_id}/layers')
def get_layers(image_id: str):
    return crud.image.get_relationships(model_id=image_id)


@api.get('/layers/<int:layer_id>')
def get_layer(layer_id: str):
    return crud.layer.get(model_id=layer_id)

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''