import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bleswplandb'