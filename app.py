from flask import Flask, jsonify, render_template
from db import MongoAPI

mongo = MongoAPI()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/clients', methods=['GET'])
def read():
    return jsonify({
                'response': mongo.read(),
                'status': '200',
            })

if __name__ == '__main__':
    app.run()