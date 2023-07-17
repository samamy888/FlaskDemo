from app import app
import os

if __name__ == '__main__':
   ## secret_key 是session要的
   app.secret_key = os.urandom(12)
   app.run('0.0.0.0')