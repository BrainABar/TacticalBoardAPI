from flask_restx import Namespace, Resource, fields

api = Namespace('maps', description='Maps for various references', title='Maps')


# Documentation for swagger
map = api.model('Map', {
    'id': fields.Integer(required=True, description='Map identifier'),
    'ref-id': fields.Integer(required=True, description='Reference that owns this map'),
    'label': fields.String(required=True, description='Maps label'),
    'img-url': fields.String(required=True, description='Bucket url of map image'),
})

reference = api.model('Reference', {
    'id': fields.Integer(required=True, description='Reference identifier'),
    'label': fields.String(required=True, description='Label given to reference'),
    'map-ids': fields.List(fields.Integer(required=True, description='Maps that belong to this reference')),
})
###########################


@api.route('/reference')
class ReferencesList(Resource):
    @api.doc('list games')
    @api.marshal_list_with(reference)
    def get(self):
        ''' List of all references '''
        return GAMES


@api.route('/reference/<id>')
@api.param('id', 'Reference identifier')
@api.response(404, 'Reference identifier not found')
class Reference(Resource):
    @api.doc('get single reference')
    @api.marshal_with(reference)
    def get(self, id):
        ''' Single reference '''
        return id


@api.route('/<id>')
@api.param('id', 'Map identifier')
@api.response(404, 'Map identifier not found')
class Map(Resource):
    @api.doc('get_map')
    @api.marshal_with(map)
    def get(self, id):
        '''  Fetch maps given identifier '''
        for item in MAPS:
            if item['id'] == id:
                return item
        api.abort(404)
