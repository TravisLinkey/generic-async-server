from celery import Celery
from time import sleep


broker_url = 'YOUR CREDS HERE'
db_url = 'db+sqlite:///db.sqlite3'

app = Celery('tasks', broker=broker_url, backend=db_url)


# Simple test function
@app.task
def reverse(text):
    time.sleep(5)
    return text[::-1]
