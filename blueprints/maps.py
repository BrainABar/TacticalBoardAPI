from flask import Blueprint
from database.data import db_session
from database.models import Reference, Map, MapImage, Layer

api = Blueprint('map api', __name__)


@api.route('/references', methods=['GET'])
def references():
    ''' List of all references '''
    references = db_session.query(Reference).all()
    return str(len(references))


@api.route('reference/<int:reference_id>', methods=['GET'])
def reference(reference_id: int):
    ''' Get A reference by id '''
    reference = db_session.query(Reference).filter(Reference.id == reference_id).one()
    return reference.label


@api.route('/reference/<int:reference_id>/maps')
def maps(reference_id: int):
    ''' List of maps associated with reference id'''
    reference = db_session.query(Reference).filter(Reference.id == reference_id).one()
    maps = reference.maps
    return str(len(maps))


@api.route('/map/<int:map_id>', methods=['GET'])
def map(map_id: int):
    ''' Get map details and list of map urls '''
    map = db_session.query(Map).filter(Map.id == map_id).one()
    return str(map.label)


@api.route('/map/<int:map_id>/urls', methods=['GET'])
def urls(map_id: int):
    ''' Get url list from map id '''
    map = db_session.query(Map).filter(Map.id == map_id).one()
    images = map.mapImages
    return str(len(images))


@api.route('url/<int:url_id>', methods=['GET'])
def url(url_id):
    ''' Get url link and details '''
    image = db_session.query(MapImage).filter(MapImage.id == url_id).one()
    return image.url

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''