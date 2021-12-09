from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import identity,authenticate
from resources.user import UserResgister
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from db import db

app = Flask(__name__)
app.secret_key='jose'

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api= Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt= JWT(app,authenticate,identity)  #/auth

        
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

api.add_resource(UserResgister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')



if __name__ == '__main__':
    app.run(port=5000,debug=True)

