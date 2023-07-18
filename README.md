# FlaskDemo
flask練習

安裝依賴
```
$ pip install -r requirements.txt
```
啟動程式
```
$ python app.py     
$ celery -A celery_worker.celery worker --loglevel=info --pool=solo
$ celery -A celery_worker.celery beat -l info -s log/celerybeat-schedule
$ flower -A celery_worker.celery --port=5555
```




[教學](https://devs.tw/post/448)
[celery教學demo](https://github.com/a607ernie/flask-celery-demo)
[IIS部屬1](https://medium.com/ai%E5%8F%8D%E6%96%97%E5%9F%8E/iis%E9%83%A8%E7%BD%B2python-web-%E4%BD%BF%E7%94%A8flask-89263dd8f945)
[IIS部屬2](https://hackmd.io/@YuXiangLiao/B1jdggdhd)