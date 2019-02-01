import requests
from bs4 import BeautifulSoup
import time
from proj.tasks import parser


t1 = time.time()

url = "http://www.wikidata.org/w/index.php?title=Special:WhatLinksHere/Q5&limit=500&from=0"
# 请求头部
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
# 发送HTTP请求
req = requests.get(url, headers=headers)
# 解析网页
soup = BeautifulSoup(req.text, "lxml")
# 找到name和Description所在的记录
human_list = soup.find(id='mw-whatlinkshere-list')('li')

urls = []
# 获取网址
for human in human_list:
    url = human.find('a')['href']
    urls.append('https://www.wikidata.org'+url)

# print(urls)

r_list = [parser.delay(url) for url in urls]

for r in r_list:
    while not r.ready():
        pass
    # print(r.ready())
    if r.result != ['', '']:
        print(r.result)


t2 = time.time() # 结束时间
print('耗时：%s' % (t2 - t1))

