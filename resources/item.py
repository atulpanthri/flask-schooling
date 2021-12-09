from typing_extensions import Required
from flask_restful import Resource,reqparse
from flask_jwt import jwt,jwt_required,request
from model.item import ItemModel

items=[]

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be empty")

    parser.add_argument("store_id",
                        type=str,
                        required=True,
                        help = "store_id cannot be empty")

    @jwt_required()
    def get(self,name):

        item = ItemModel.get_item_by_name(name)

        if item:
            return  item.json(),201

        return {'message':"Item not found"}, 404

    def post(self,name):

        Item.parser.parse_args()
        request_data = request.get_json()

        if ItemModel.get_item_by_name(name):
            return {'message':'item already exists'},404

        item = ItemModel(name, **request_data)

        #try:

        item.save_to_db()
        
        #except:
        #    return {'message':'some error occurred'},500
        
        return item.json(),201

    def delete(self,name):
        item = ItemModel.get_item_by_name(name)

        item.delete()
        return {'message':'item deleted'}

    def put(self,name):

        request_data = Item.parser.parse_args()

        item = ItemModel.get_item_by_name(name)

        if item:
            item.price = request_data['price']
            item.store_id = request_data['store_id']
        else:
            item = ItemModel(name,**request_data)
        
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item'},500

        return item.json(),201

class ItemList(Resource):

    def get(self):
        
        return {'items': list(map(lambda x: x.json(),ItemModel.query.all())) }