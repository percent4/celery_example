from proj.app_test import app


@app.task
def taskA(x, y):
    return x * y


@app.task
def taskB(x, y, z):
    return x + y + z


@app.task
def add(x, y):
    return x + y