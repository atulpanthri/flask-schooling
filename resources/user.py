from typing_extensions import Required
from flask_restful import Resource,reqparse
from model.item import ItemModel

from model.user import *

class UserResgister(Resource):
    parse = reqparse.RequestParser()
    
    parse.add_argument('username',
                       type=str,
                       required=True,
                       help="This field cannot be blank"
                       )
    
    parse.add_argument('password',
                        type=str,
                        required = True,
                        help='This field cannot be blank')

    def post(self):
        
        data = UserResgister.parse.parse_args()

        if UserModel.find_by_name(data['username']):
            return {'message': 'user with same name already exists'},400

        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        
        return {'message':'user has been registered'}
