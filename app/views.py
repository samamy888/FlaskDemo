from flask import Flask, render_template,request, redirect, url_for, jsonify, abort , json, session, flash, abort

from app import app

@app.route('/')
def index():
    # schedule_task.apply_async(countdown=10, repeat=True)
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route("/logout", methods=['GET'])
def logout():
    session['logged_in'] = False
    session['accountId'] = None
    session['admin'] = False
    return redirect(url_for('login'))

@app.route('/loginAction', methods=['POST'])
def loginAction():
    error = None
    data = request.get_json()
    # with open('static/data/account.json', 'r') as f:
    #         data = json.load(f)
    #         print("text : ", data)
    if (data['account'] != 'admin' or data['password'] != 'admin') and (data['account'] != 'user' or data['password'] != 'user'):
        error = '帳密錯誤'
        abort_with_error(401, error)
    else:
        print(data)
        session['logged_in'] = True
        session['accountId'] = data['account']
        session['admin'] = True
        return jsonify(data['account'])

@app.errorhandler(400)
@app.errorhandler(401)
def handle_error(error):
    response = jsonify({'error': error.description})
    response.status_code = error.code
    return response

def abort_with_error(code, message):
    description = message
    response = jsonify({'error': description})
    response.status_code = code
    abort(response)
