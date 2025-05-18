from flask import Flask
from flask import request #抓login form datas
from flask import render_template #go xxx.html
from flask import redirect, url_for #redirect to xxx > /xxx
import dataset  #database

app = Flask(__name__)

# 連接到 SQLite 數據庫，如果數據庫不存在，則會自動創建
db = dataset.connect('sqlite:///file.db')

# 創建一個表格，名稱為 'userplay'
table = db['userplay']

# 一開網頁會出現login.html的頁面
@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

# 按下 login.html 中 form Submit 後會將資料(name、message)
# 以 HTTP POST 方式送到 /submit 這個網址，然後出現 wp.html 的頁面
    # 字典 dict 有兩個資料欄位(name、message)，分別存放從 login form 抓來的資料再存入 data
    # 將 data 存入 DB 的 table
@app.route('/submit', methods=['POST'])
def submit():
    data = dict(name=request.form['name'], message=request.form['message'])
    table.insert(data)
    return redirect(url_for('up'))

@app.route('/up', methods=['GET'])
def up():
    datas = table.find()
    table.delete(name='')
    return render_template('up.html', datas=datas)

#@app.route('/submit', methods=['POST'])
#def submit():
    # 傳到up.html
#    return render_template('Wp.html')

#@app.route('/wp', methods=['GET'])
#def login():
#    return render_template('wp.html')

#@app.route('/wp', methods=['POST'])
#def wp():
    #結束遊戲>紀錄>回傳紀錄關卡>紀錄回傳到up
#    return redirect(url_for('up'))

#@app.route('/up', methods=['GET'])
#def wp():
    #結束遊戲>紀錄>回傳紀錄關卡>紀錄回傳到up
#    return  render_template('up.html')

for i in table.all():
    print(i)

delete = table.delete()

if __name__ == '__main__':
    app.run()