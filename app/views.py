from app import app
from flask import jsonify
from flask_pymongo import PyMongo
from app.modules.semantic import math2chin

mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/api/semanticAPI/<int:math_id>', methods=['GET'])
def get_math2chin(math_id):
    chin_id = math2chin.math2ch(math_id)
    
    response = {
        'status': 200,
        'msg': '請求成功',
        'result': chin_id
    }
    
    return jsonify(response)

@app.route('/api/goodsAPI/', methods=['GET'])
def get_goodsList():
    goods = mongo.db.goods.find()
    
    good_list = []
    for good in goods:
        good.pop('_id')
        good_list.append(good)
        
    response = {
        'status': 200,
        'msg': '請求成功',
        'result': good_list
    }
    return jsonify(response)
