from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

#pymongo 계정 접속 id:passwprd
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name_give']
    count = request.form['count_give']
    adress = request.form['adress_give']
    phone = request.form['phone_give']

    doc = {
        'name' : name,
        'count' : count,
        'adress' : adress,
        'phone' : phone
    }
    db.orders.insert_one(doc)
    return jsonify({'msg': '주문이 완료되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))

    return jsonify({'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)