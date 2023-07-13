from flask import Flask, render_template,request, redirect, url_for, jsonify, abort , json, session, flash, abort
from app import app

@app.route('/')
def index():
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
