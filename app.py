from flask import Flask, jsonify, render_template, request
from db import MongoAPI

mongo = MongoAPI()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/clients', methods=['GET'])
def read():
    return (mongo.read(), 200)

@app.route('/clients', methods=['POST'])
def write():
    client = mongo.write(request.json)
    client['_id'] = str(client['_id'])
    return (jsonify(client), 201)

if __name__ == '__main__':
    app.run()