from flask_restx import Api
from apis.maps import api as maps_namespace

api = Api(
    title='Title',
    version='0.1',
    description='description',
)

api.add_namespace(maps_namespace)
