from app import app
from flask import jsonify, session, request, Blueprint
from config import BASE_DIR, client

base = Blueprint('base', __name__)

# 連進MongoDB
db = client['name_db']

@app.route('/api/login', methods=['POST'])
def login():
    '''網頁端登入, 使用SESSION記錄登入
    Params:
        account: 登入帳號
        pwd: 登入密碼
    Returns:
        {
            'result': name, account, dept
            'msg': ''
        }
    '''
    
    account = request.json['account']
    pwd = request.json['pwd']

    # 查看資料庫是否有此帳號
    user_collect = db['users']
    user_doc = user_collect.find_one({'account': account, 'pwd': pwd})

    if user_doc is None:
        resp = {
            'result': '',
            'msg': '沒有此帳號'
        }
        return jsonify(resp), 404
    else:
        # 記錄到session
        session['login'] = True
        session['account'] = user_doc['account']

        obj = {
            'name': user_doc['name'],
            'account': user_doc['account']
        }

        resp = {
            'result': obj,
            'msg': '登入成功'
        }
        return jsonify(resp), 200


@app.route('/api/logout', methods=['POST'])
def logout():
    '''登出, 刪除SESSION內的紀錄
    Returns:
        {
            'result': ''
            'msg': 訊息
        }
    '''

    if(session.get('login') != None):
        # 刪除session
        session.pop('login', None)
        session.pop('account', None)

        resp = {
            'result': '',
            'msg': '登出成功'
        }
        return jsonify(resp), 200
    else:
        resp = {
            'result': '',
            'msg': '原本就沒有此登入紀錄, 登出失敗'
        }
        return jsonify(resp), 404


@app.route('/api/checkLogin', methods=['GET'])
def checkLogin():
    '''檢查是否登入
    Returns:
        {
            'result': 正在登入的account; 錯誤訊息
            'msg': account登入中
        }
    '''

    try:
        if session.get('login') == True:
            obj = {
                'status': True,
                'account': session['account']
            }

            resp = {
                'result': obj,
                'msg': session['account']+'登入中'
            }
            return jsonify(resp), 200
        else:
            obj = {
                'status': False,
                'dept': '',
                'account': ''
            }

            resp = {
                'result': obj,
                'msg': '未登入'
            }
            return jsonify(resp), 200
    except Exception as err:
        resp = {
            'result': '',
            'msg': str(err)
        }
        return jsonify(resp), 404
