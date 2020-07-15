from proj.app_test import app
import datetime
from random import randint


@app.task
def add(x, y):
    a = randint(x, y)
    b = randint(x, y)
    return "%s + %s = %s" % (a, b, a+b)

@app.task
def time_teller():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")