from celery import Celery
from time import sleep


with f as open('creds.txt', 'r'):
    broker_url = f.read()

db_url = 'db+sqlite:///db.sqlite3'
app = Celery('tasks', broker=broker_url, backend=db_url)


@app.task
def reverse(text):
    time.sleep(5)
    return text[::-1]
