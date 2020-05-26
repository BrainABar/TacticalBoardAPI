from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/maps', methods=['GET'])
def maps():

    maps = []

    return jsonify({'maps': maps})
