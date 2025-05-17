from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/wp')
def wp():
    return render_template('wp.html')

@app.route('/submit', methods=['POST'])
def submit():
    return redirect(url_for('wp'))


if __name__ == '__main__':
    app.run(debug=True)