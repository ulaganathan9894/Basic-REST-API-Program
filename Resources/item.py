import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.item import ItemModel

class Item(Resource):
    #TABLE_NAME = 'items'
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type = float,
                        required = True,
                        help = 'the field cannot be left !'
                        )
    parser.add_argument('store_id',
                        type = int,
                        required = True,
                        help = 'Every item need a store id !'
                        )
    


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message' : 'item not found'}, 404


    #@jwt_required() 
    def post(self, name):
        if ItemModel.find_by_name(name):
            return{'Message':'the item {} is already exist.' .format(name)}, 400 
        request_data = Item.parser.parse_args()#request.get_json(silent = True)
        item =ItemModel(name, **request_data)#request_data['price'], request_data['store_id']
        try:
            item.save_db()
        except:
            return {"message": "An error occured inserting the item."}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_db()
        return {'Message':'Item Successfully Deleted'}     

            
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "DELETE FROM items WHERE name = ?"
##        val = cursor.execute(query, (name,))
##        row = val.fetchone()
##        connection.commit()
##        connection.close()
##        return{'Message':'item deleted'}


    def put(self, name):
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)#next(filter(lambda x: x['name'] == name, items),None)
        if item is None:
            item = ItemModel(name,**request_data)#request_data['price'], request_data['store_id']
        else:
            item.price = request_data['price']
        item.save_db()
        
        return item.json()


class Itemlist(Resource):
    def get(self):
        return {'items' : [x.json() for x in ItemModel.query.all()]}
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "SELECT * FROM items"
##        value = cursor.execute(query)
##        items = []
##        for row in value:
##            items.append({'name': row[0], 'price': row[1]})
##        connection.close()
##        return {'items': items}
         
