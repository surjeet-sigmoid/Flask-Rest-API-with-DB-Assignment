from flask import Flask, request, jsonify

from modal import Product
from database import db,ma
import os
# from util.script import create_script,get_Data

# Init app
# def get_app():
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db.init_app(app)
ma.init_app(app)
    # return app
# app=get_app()

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'status', 'copy_right', 'num_result', 'last_modified','results')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route("/addlist",methods=["POST"])
def addList():
    # id = request.json["id"]
    status = request.json["status"]
    copy_right = request.json["copy_right"] 
    num_result = request.json["num_result"]
    last_modified = request.json["last_modified"]
    results = request.json["results"]
    
    db.create_all();
    new_book=Product(status,copy_right,num_result,last_modified,results)
    db.session.add(new_book)
    db.session.commit()
    return product_schema.jsonify(new_book)
    
@app.route("/list",methods=["GET"])   
def getList():
    all_books=Product.query.all()
    result=products_schema.dump(all_books)
    return jsonify(result)
     

if __name__ == "__main__":
    app.run(port=5001, debug = True)
  


# class Owner(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
    
# def addOwner():
#     db.create_all()
#     add_obj = Owner(name = "vikash")
#     db.session.add(add_obj)
#     db.session.commit()
    

# @app.route('/')
# def home():
#     return "homepage"
# @app.route('/addowner')
# def addOwner():
#     addOwner()
#     return "owner created"

# @app.route('/getowner')
# def getOwner():
#     owner_obj = Owner.query.first()
#     #return "vikash"
#     return {"id" : owner_obj.id, "name" : owner_obj.name}
    
# if __name__ == "__main__":
#     app.run(port=5001,debug=True)
    
    





# # Init ma
# #ma = Marshmallow(app)

# # Product Class/Model
