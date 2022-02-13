from pyrenaper.utils import BarcodeReader
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import User
from parsers import sid_parser
from utils import resize, call_sid_api
from flask_cors import CORS
from flask_restful import Resource, Api
import bson

app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongo',
    'db': 'renaper',
    'username': 'docker',
    'password': 'docker'
    
}
api = Api(app)


initialize_db(app)    


class UserResource(Resource):
    parser = sid_parser

    def get(self, transaction_id):
        if bson.ObjectId.is_valid(transaction_id):
            user = User.objects.get_or_404(id=transaction_id)
            return {"data": user.data, "status": user.status}, 200
        return {"message": "Object not Found"}, 404
    
    def post(self, transaction_id):
        user = User.objects(user_id=transaction_id).first()
        if not user:
            user =  User(user_id=transaction_id, status='created').save()        
        return {"transaction_id": str(user.id)}, 200

    def put(self, transaction_id):
        if not bson.ObjectId.is_valid(transaction_id):
            return {"message": "Error decoding id"}, 400
        
        user = User.objects.get_or_404(id=transaction_id)
        
        if user.status not in ['created', 'error']:
            return {"message": "User status is not valid, please refresh user data"}, 400

        args = self.parser.parse_args()
        front = resize(args['front'], 1200)
        barcode_reader = BarcodeReader()
        user_data = barcode_reader.get_barcode_payload(front)
        data, status =  call_sid_api('get_full_person_data', user_data['number'],
                                                             user_data['gender'],
                                                             user_data['order'])
        if not data['status']:
            user.update(status='error', data={"message": data['description']})
        else:
            user.update(data=data, status='success')
        user.reload()
        return {"data": user.data, "status": user.status}, 200

class BarcodeParserResource(Resource):
    parser = sid_parser

    def post(self):
        args = self.parser.parse_args()
        front = resize(args['front'], 1200)
        barcode_reader = BarcodeReader()
        user_data = barcode_reader.get_barcode_payload(front)
        return user_data, 200
    
api.add_resource(UserResource, '/user/<transaction_id>')
api.add_resource(BarcodeParserResource, '/decode/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

