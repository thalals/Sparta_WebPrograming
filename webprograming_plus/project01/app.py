from flask import Flask, render_template,request,jsonify
from datetime import datetime

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_plus_week1

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():

    diaries = list(db.diary.find({}, {'_id': False}))
    print(diaries)
    return jsonify({'articles': diaries})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form['title_give']
    contents_receive = request.form['content_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]
    today = datetime.now()

    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

    filename = f'file-{mytime}'
    save_to = f'static/{filename}.{extension}'
    file.save(save_to)

    doc={
        'title' : title_receive,
        'content' : contents_receive,
        'file':f'{filename}.{extension}',
        'time':mytime
    }

    db.diary.insert_one(doc)

    return jsonify({'msg': 'POST 요청 완료!'})


if __name__ == '__main__':
    app.run()
