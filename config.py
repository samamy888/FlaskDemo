import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

Account = [{
    'account' : 'admin',
    'password' : 'admin',
    'admin' : True
},
{
    'account' : 'user',
    'password' : 'user',
    'admin' : False
},
]