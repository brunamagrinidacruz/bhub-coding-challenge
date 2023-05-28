from flask import Flask, jsonify, render_template, request, abort, make_response
from db import MongoAPI
from bson.objectid import ObjectId
import re

mongo = MongoAPI()
app = Flask(__name__)

def is_client_id_valid(client_id):
    return ObjectId.is_valid(client_id)

def is_client_complete(client):
    if 'company_name' not in client:
        return (False, "missing company_name")
    if 'telephone' not in client:
        return (False, "missing telephone")
    if 'address' not in client:
        return (False, "missing address")
    if 'declared_billing' not in client:
        return (False, "missing declared_billing")
    if 'bank_accounts' not in client:
        return (False, "missing bank_accounts")
    if len(client['bank_accounts']) == 0:
        return (False, "empty bank_accounts")
    for bank_account in client['bank_accounts']:
        if 'bank' not in bank_account:
            return (False, "missing bank")
        if 'agency' not in bank_account:
            return (False, "missing agency")
        if 'account_number' not in bank_account:
            return (False, "missing account_number")
    return (True, None)
    
def is_client_valid(client):
    if 'telephone' in client:
        telephone_regex = re.compile(r'^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$')
        if not (re.fullmatch(telephone_regex, client['telephone'])):
            return (False, "telephone not well formated")
    if 'declared_billing' in client:
        if not isinstance(client['declared_billing'], (int, float)):
            return (False, "declared_billing wrong type")
    if 'bank_accounts' in client:
        for bank_account in client['bank_accounts']:
            bank_regex = re.compile(r'^[0-9]{3,3}')
            if not (re.fullmatch(bank_regex, bank_account['bank'])):
                return (False, "bank not well formated")
            agency_regex = re.compile(r'^[0-9]{3,5}')
            if not (re.fullmatch(agency_regex, bank_account['agency'])):
                return (False, "agency not well formated")
            account_number_regex = re.compile(r'^[0-9]{1,20}\-[0-9|a-z|A-Z]')
            if not (re.fullmatch(account_number_regex, bank_account['account_number'])):
                return (False, "account_number not well formated")
    return (True, None)

@app.route('/', methods=['GET'])
def index():
    return make_response(render_template('index.html'), 200)

@app.route('/clients', methods=['GET'])
def read():
    return make_response(mongo.read(), 200)

@app.route('/clients/<client_id>', methods=['GET'])
def readOne(client_id):
    if (not is_client_id_valid(client_id)):
        return make_response(jsonify({"error": "invalid id"}), 400)

    client = mongo.readOne({ '_id': ObjectId(client_id)})
                  
    if client is None:
        abort(404)

    client['_id'] = str(client['_id'])
    return (make_response(jsonify(client)), 200)

@app.route('/clients', methods=['POST'])
def create():
    is_complete, error = is_client_complete(request.json)
    if (not is_complete):
        return make_response(jsonify({"error": error}), 400)
    is_valid, error = is_client_valid(request.json)
    if (not is_valid):
         return make_response(jsonify({"error": error}), 400)
 
    client = mongo.create(request.json)
    client['_id'] = str(client['_id'])

    return make_response(jsonify(client), 201)

@app.route('/clients/<client_id>', methods=['PUT'])
def update(client_id):
        if (not is_client_id_valid(client_id)):
            return make_response(jsonify({"error": "invalid id"}), 400)
        is_valid, error = is_client_valid(request.json)
        if (not is_valid):
         return make_response(jsonify({"error": error}), 400)

        modified, client = mongo.update({ '_id': ObjectId(client_id)}, request.json) 

        if (not modified):
            abort(404)
        
        client['_id'] = str(client['_id'])
        return make_response(jsonify(client), 200) 

@app.route('/clients/<client_id>', methods=['DELETE'])
def delete(client_id):
    if (not is_client_id_valid(client_id)):
        return make_response(jsonify({"error": "invalid id"}), 400)

    deleted = mongo.delete({ '_id': ObjectId(client_id)}) 

    if (not deleted):
        abort(404)

    return make_response("", 204)

if __name__ == '__main__':
    app.run()