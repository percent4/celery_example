from proj.app_test import app
import time
import re
import requests

@app.task
def add(x, y):
    time.sleep(1)
    return x + y

@app.task
# 获取每个网页的name和description
def parser(url):
    req = requests.get(url)
    html = req.text
    try:
        name = re.findall(r'<span class="wikibase-title-label">(.+?)</span>', html)[0]
        desc = re.findall(r'<span class="wikibase-descriptionview-text">(.+?)</span>', html)[0]
        if name is not None and desc is not None:
            return name, desc
    except Exception as  err:
        return '', ''