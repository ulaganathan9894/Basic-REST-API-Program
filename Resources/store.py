from flask_restful import Resource
from Models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'Message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'Message' : 'Store name {} already exists.'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_db()
        except:
            return {'Message' : 'An Error Occuured While creating store'}
        return store.json(), 201
        
       
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store = StoreModel.delete_db()

        return {'Message' : 'Store deleted'}    

class StoreList(Resource):
    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all()]}
        
