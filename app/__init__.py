from flask import Flask,Blueprint,send_from_directory
from celery import Celery
import os
import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

# 创建 Celery 实例
celery = Celery(__name__)
celery.config_from_object('tasks.celeryconfig')

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# import module
from app.api.testapi import testapi
from app.api.test_add import test_add
# register blueprint
app.register_blueprint(testapi)
app.register_blueprint(test_add)


#######################################
##define log config and create log folder
#######################################
if os.path.isdir('log') == False:
    os.mkdir('log')
if os.path.isfile('./log/flask.log') == False:
    with open("./log/flask.log",'w') as f:
        f.close()
#====================================logging config======================================
formatter = logging.Formatter("[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
handler = TimedRotatingFileHandler("log/flask.log", when="D", interval=1, backupCount=15,encoding="UTF-8", delay=False, utc=True)
app.logger.addHandler(handler)
handler.setFormatter(formatter)
#====================================logging config======================================

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

