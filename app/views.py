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

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['accountId'] = None
    session['admin'] = False
    return redirect(url_for('index'))

@app.route('/loginAction', methods=['POST'])
def loginAction():
    error = None
    data = request.get_json()
    if data['account'] != 'admin' or data['password'] != 'admin':
        error = 'Invalid Credentials. Please try again.'
        abort_with_error(401, error)
    else:
        print(data)
        session['logged_in'] = True
        session['accountId'] = data['account']
        session['admin'] = True
        flash('Successful login.')
        return jsonify()

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
