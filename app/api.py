from flask_restful import Resource

from app import api
from schemes import UserScheme


class UserApi(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}

    def put(self):
        return {'hello': 'world'}

    def delete(self):
        return {'hello': 'world'}


api.add_resource(UserApi, '/')
