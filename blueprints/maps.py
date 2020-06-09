from flask import Blueprint
from database.models import Reference, Map

api = Blueprint('map api', __name__)


@api.route('/references', methods=['GET'])
def references():
    ''' List of all references '''
    return '123'


@api.route('reference/<int:reference_id>', methods=['GET'])
def reference(reference_id: int):
    ''' Get A reference by id '''
    return str(reference_id)


@api.route('/reference/<int:reference_id>/maps')
def maps(reference_id: int):
    ''' List of maps associated with reference id'''
    return str(reference_id)


@api.route('/map/<int:map_id>', methods=['GET'])
def map(map_id: int):
    ''' Get map details and list of map urls '''
    return str(map_id)


@api.route('/map/<int:map_id>/urls', methods=['GET'])
def urls(map_id: int):
    ''' Get url list from map id '''
    return str(map_id)


@api.route('url/<int:url_id>', methods=['GET'])
def url(url_id):
    ''' Get url link and details '''
    return str(url_id)

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''