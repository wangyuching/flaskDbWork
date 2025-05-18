from flask import Flask, request, session, render_template, redirect, url_for
import datetime
import dataset

app = Flask(__name__)
app.secret_key ='a'#亂數

db = dataset.connect('sqlite:///file.db')
table = db['userplay']

@app.route('/', methods=['GET'])
def login():
    if table.count() >= 5:
        table.delete()
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form['name']

    if len(name) == 0:
        return render_template('index.html', hint='!!!NAME!!!')
    
    if len(name) == 0:
        name = 'NONE'

    session['temp_data'] = {'st': time, 'n': name}
    return render_template('wp.html')

@app.route('/finish', methods=['POST'])
def finish():
    finishLevel = request.form.get('finish-level-input')

    temp_data = session.get('temp_data',{})
    temp_data['fl'] = finishLevel
    session['temp_data'] = temp_data

    table.insert(temp_data)

    return redirect(url_for('up'))

@app.route('/up', methods=['GET'])
def up():
    datas = table.find()
    total = table.count()
    return render_template('up.html', datas=datas, total=total)

if __name__ == '__main__':
    app.run()