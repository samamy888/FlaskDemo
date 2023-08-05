from flask import render_template
from app import app
from app.database import db

@app.route('/')
def index():
    result = db.getDBList()
    print(result)
    result2 = db.testDBListDetail()
    print(result2)
    return render_template('index.html')
