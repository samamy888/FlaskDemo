from flask import render_template
from app import app
from app.database import db

@app.route('/')
def index():
    result = db.getDBList()
    print(result)
    return render_template('index.html')
