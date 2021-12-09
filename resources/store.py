from model.store import StoreModel
from flask_restful import Resource


class Store(Resource):
    
    def post(self,name):
        
        if StoreModel.find_store_by_name(name):
            return {'message':f'{name} store already exists'},404
        
        try:

            store = StoreModel(name)
            store.save_to_db()
            
        except:
            return {'message':'some error occurred while saving'},500
        
        return store.json(),200


    def get(self,name):

        store = StoreModel.find_store_by_name(name)

        if store:
            return store.json(),200
        
        return {'message':f'{name} Store not found'},404

            
    def delete(self,name):

        store =  StoreModel.find_store_by_name(name)

        if store:
            store.delete_from_db()
            return{'message':f'{name} store deleted'}
            
        return {'message':f'{name} store not found'}

class StoreList(Resource):
    def get(self):

        return {'stores':[store.json() for store in StoreModel.query.all()]}