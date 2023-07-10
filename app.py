from flask import Flask, render_template,request, redirect, url_for, jsonify, json
from werkzeug.debug import DebuggedApplication
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/page/text')
def pageText():
    return render_template('page.html', text="Python Flask !")

@app.route('/page/app')
def pageAppInfo():
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    return render_template('page.html', appInfo=appInfo)

@app.route('/page/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('page.html', data=data)

@app.route('/static')
def staticPage():
    return render_template('static.html')

@app.route('/form')
def formPage():
    return render_template('Form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        return redirect(url_for('success', name=user, action="post"))
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        return redirect(url_for('success', name=user, action="get"))

@app.route('/success/<action>/<name>')
def success(name, action):
    return '{} : Welcome {} ~ !!!'.format(action, name)

@app.route('/data')
def webapi():
    return render_template('data.html')

@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)  # 直接回傳 data 也可以，都是 json 格式

@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'id': request.form['app_id'],
                'name': request.form['app_name'],
                'version': request.form['app_version'],
                'author': request.form['app_author'],
                'remark': request.form['app_remark']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')

if __name__ == '__main__':
    app.debug = True
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    app.run('0.0.0.0',debug=true)