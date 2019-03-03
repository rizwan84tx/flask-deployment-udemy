from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #flask_SQLAlchemy tracks all changes takes more resources, we turn it OFF as SQLAlchemy has its own library that does tracking
app.secret_key = 'rizwan' #key to excrypt the data
api = Api(app)

jwt =  JWT(app, authenticate, identity) #/auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=2605, debug=True)
