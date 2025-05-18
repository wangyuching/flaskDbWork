from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 傳到up.html
    return render_template('up.html')

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

if __name__ == '__main__':
    app.run()