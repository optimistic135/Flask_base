from flask import Blueprint, jsonify

bule = Blueprint('bule',__name__)

@bule.route('/')
def index():
    return jsonify({
        'msg' : 'welcome to example'
    })

@bule.route('/buleprint')
def test_buleprint():
    return jsonify({
        "msg" : "this is buleprint for esay dev!"
    })