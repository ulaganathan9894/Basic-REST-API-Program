from flask import Flask, request
from flask_restful import Api
#from flask_httpauth import HTTPBasicAuth
from flask_jwt import JWT

from security import authenticate, identity
from Resources.user import Register
from Resources.item import Item, Itemlist
from Resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rome'
#app.config['JWT_AUTH_USERNAME_KEY'] = 'rome'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')               
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(Register, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port = 5000, debug = True)
