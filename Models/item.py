import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
         return {'name' : self.name, 'price' : self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name = name).first() #SELECT * FROM items WHERE name = ? LIMIT =1
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "SELECT * FROM items WHERE name = ?"#.format(table=cls.TABLE_NAME)
##        val = cursor.execute(query, (name,))
##        row = val.fetchone()
##        #connection.commit()
##        connection.close()

##        if row:
##            return cls(*row)
        #return {'message':'item not found'}, 404

##        item = next(filter(lambda x: x['name'] == name, items),None)
##        return {'item' : item}, 200 if item else 404

    def save_db(self):
        db.session.add(self)
        db.session.commit()
##        connection = sqlite3.connect('data.db')
##        cursor = connection.cursor()
##        query = "INSERT INTO items VALUES(?, ?)"#.format(table=cls.TABLE_NAME)
##        cursor.execute(query, (self.name, self.price))
##        connection.commit()
##        connection.close()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()
 
