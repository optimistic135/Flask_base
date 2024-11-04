from flask_restful import request, Resource

class result_class(Resource):
    def get(self):
        return {'message': 'Hello, This is restful GET'}

    def post(self):
        data = request.json
        name = data.get('name', None)
        return {'message': f'Hello {name}, This is restful POST'}

    def put(self):
        pass

    def detele(self):
        pass