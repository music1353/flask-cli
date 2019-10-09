from app import app
from flask import jsonify, session, request
from config import BASE_DIR, client

# 連進MongoDB
db = client['name_db']

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/api/xxx', methods=['GET'])
def get_xx(math_id):
    obj = {}
    
    response = {
        'status': 200,
        'msg': '請求成功',
        'result': obj
    }
    
    return jsonify(response)