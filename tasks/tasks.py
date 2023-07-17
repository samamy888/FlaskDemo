from celery import Celery

app = Celery(
    'myapp',
    broker='memory://',
    backend='cache://'
)

def process_task(arg1, arg2):
    result = arg1 + arg2
    return result