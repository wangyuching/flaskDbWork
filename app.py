from flask import Flask, request, session, render_template, redirect, url_for #模組
import datetime #時間模組
import dataset #資料庫模組

app = Flask(__name__)
app.secret_key ='adgjlshkasdfghjkl' #session密碼(隨便寫)

db = dataset.connect('sqlite:///file.db') #連接資料庫
table = db['userplay'] #資料表名稱

@app.route('/', methods=['GET'])
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    name = request.form['name']

    if len(name) == 0:
        return render_template('index.html', hint='!!!NAME!!!')

    exist = table.find_one(n=name)
    if exist:
        return render_template('index.html', hint='!!!名稱已存在，請重新輸入!!!')

    session['temp_data'] = {'st': time, 'n': name}
    return render_template('wp.html')

@app.route('/finish', methods=['POST'])
def finish():
    finishLevel = request.form.get('finish-level-input')

    temp_data = session.get('temp_data',{})
    temp_data['fl'] = finishLevel
    session['temp_data'] = temp_data

    all_data = list(table.all())
    if table.count() >=5:
        max_level = max([int(i['fl']) for i in all_data])
        max_level_records = [i for i in all_data if int(i['fl']) == max_level]
        keep_record = max(max_level_records, key=lambda x: x['st'])
        for record in all_data:
            if record['id'] != keep_record['id']:
                table.delete(id=record['id'])

    table.insert(temp_data)

    return redirect(url_for('up'))

@app.route('/up', methods=['GET'])
def up():
    datas = table.find()
    return render_template('up.html', datas=datas)

if __name__ == '__main__':
    app.run()