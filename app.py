from flask import Flask, jsonify, render_template, request, abort, make_response
from db import MongoAPI
from bson.objectid import ObjectId

mongo = MongoAPI()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return make_response(render_template('index.html'), 200)

@app.route('/clients', methods=['GET'])
def read():
    return make_response(mongo.read(), 200)

@app.route('/clients', methods=['POST'])
def create():
    client = mongo.create(request.json)
    client['_id'] = str(client['_id'])
    return make_response(jsonify(client), 201)

@app.route('/clients/<client_id>', methods=['PUT'])
def update(client_id):
        modified, client = mongo.update({ '_id': ObjectId(client_id)}, request.json) 
        
        if (not modified):
            abort(404)
        
        client['_id'] = str(client['_id'])
        return make_response(jsonify(client), 200) 

@app.route('/clients/<client_id>', methods=['DELETE'])
def delete(client_id):
    deleted = mongo.delete({ '_id': ObjectId(client_id)}) 
    if (not deleted):
        abort(404)

    return make_response("", 204)

if __name__ == '__main__':
    app.run()