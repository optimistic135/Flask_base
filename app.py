from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from models.bule_print import bule
from models.restful_class import result_class

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

@app.route('/')
def index():
    return jsonify({
        "msg":"welcome to flask_base"
    }), 200

app.register_blueprint(bule, url_prefix='/example')
api.add_resource(result_class, '/result_class')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)