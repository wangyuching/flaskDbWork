from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for
import datetime
import dataset

app = Flask(__name__)

db = dataset.connect('sqlite:///file.db')

table = db['userplay']

@app.route('/', methods=['GET'])
def login():
    if table.count() >= 5:
        table.delete()
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form['name']
    message = request.form['message']

    if len(name) == 0 and len(message) == 0:
        return render_template('login.html', hint='!!!至少其中一個欄位要有東西!!!')
    
    if len(name) == 0:
        name = 'NONE'

    if len(message) == 0:
        message = 'LAZZY PEOPLE'
        
    data = dict(st=time,n=name,m=message)
    table.insert(data)
    return redirect(url_for('up'))

@app.route('/up', methods=['GET'])
def up():
    datas = table.find()
    total = table.count()

    return render_template('up.html', datas=datas, total=total)

if __name__ == '__main__':
    app.run()