from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sys
from app import app

db = SQLAlchemy(app)

class dblist(db.Model):
    Id = db.Column(db.Integer,unique=True,nullable=False,primary_key=True)
    IP = db.Column(db.String(100),unique=True,nullable=False)
    Port = db.Column(db.Integer,unique=True,nullable=False)
    Account = db.Column(db.String(100),unique=True,nullable=False)
    Password = db.Column(db.String(100),unique=True,nullable=False)
    Status = db.Column(db.Integer,unique=True,nullable=True)
    
    def __init__(self, IP, Port,Account,Password,Status):
        self.IP = IP
        self.Port = Port
        self.Account = Account
        self.Password = Password
        self.Status = Status

class tempTable(db.Model):
    Id = db.Column(db.Integer,primary_key=True)
    def __init__(self, IP):
        self.IP = IP
    
def getDBList():
    all_dblist = dblist.query.all()
    db_list = list(map(lambda item: {
        'Id': item.Id,
        'IP': item.IP,
        'Port': item.Port,
        'Account': item.Account,
        'Password': item.Password,
        'Status': getDBListStatus(item.Status)
    }, all_dblist))
    return db_list

def testDBListDetail():
    dbListExist = dblist.query.first()
    db.session.close_all()
    db.engine.dispose()
    connecting = f'mysql+pymysql://{dbListExist.Account}:{dbListExist.Password}@{dbListExist.IP}:{dbListExist.Port}/'
    print(connecting)
    try :
        db.create_all()
        data = tempTable('1')
        db.session.add(data)
        db.session.commit()
        # tempTable.__table__.drop(dynamic_db.engine)
        # db.Status = 1
        # db.session.commit()
        return 1
    except Exception as e:
        print(e)
        dbListExist.Status = -1
        db.session.commit()
        return 0
    

def getDBListStatus(val):
    if val == 1:
        return "成功"
    elif val == 0 :
        return "未測試"
    else :
        return "失敗"