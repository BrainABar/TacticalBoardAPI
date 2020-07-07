from flask import Blueprint
from flask_cors import CORS
from database.data import db_session
from database.models.reference import Reference
from database.models.map import Map
from database.models.mapimage import MapImage
from database.models.layer import Layer
from database.schema import ReferenceSchema, MapSchema, ImageSchema, LayerSchema

api = Blueprint('map api', __name__)
CORS(api)


@api.route('/references', methods=['GET'])
def references():
    ''' List of all references '''
    references = db_session.query(Reference).all()
    schema = ReferenceSchema(many=True)
    result = schema.dumps(references)
    return result


@api.route('references/<int:reference_id>', methods=['GET'])
def reference(reference_id: int):
    ''' Get A reference by id '''
    reference = db_session.query(Reference).filter(Reference.id == reference_id).first()
    schema = ReferenceSchema()
    result = schema.dumps(reference)
    return result


@api.route('/references/<int:reference_id>/maps')
def maps(reference_id: int):
    ''' List of maps associated with reference id'''
    maps = db_session.query(Map).filter(Reference.id == reference_id).all()
    schema = MapSchema(many=True)
    results = schema.dumps(maps)
    return results


@api.route('/maps/<int:map_id>', methods=['GET'])
def singleMap(map_id: int):
    ''' Get map details and list of map urls '''
    map = db_session.query(Map).filter(Map.id == map_id).first()
    schema = MapSchema()
    result = schema.dumps(map)
    return result


@api.route('/maps/<int:map_id>/images', methods=['GET'])
def images(map_id: int):
    ''' Get url list from map id '''
    images = db_session.query(MapImage).filter(Map.id == map_id).all()
    schema = ImageSchema(many=True)
    results = schema.dumps(images)
    return results


@api.route('/images/<int:image_id>', methods=['GET'])
def image(image_id: int):
    ''' Get url link and details '''
    image = db_session.query(MapImage).filter(MapImage.id == image_id).first()
    schema = ImageSchema()
    result = schema.dumps(image)
    return result


@api.route('/images/<int:image_id>/layers', methods=['GET'])
def layers(image_id: int):
    layers = db_session.query(Layer).filter(MapImage.id == image_id).all()
    schema = LayerSchema(many=True)
    results = schema.dumps(layers)
    return results


@api.route('/layers/<int:layer_id>', methods=['GET'])
def layer(layer_id: int):
    layer = db_session.query(Layer).filter(Layer.id == layer_id).first()
    schema = LayerSchema()
    result = schema.dumps(layer)
    return layer_id



'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''