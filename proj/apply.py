# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020/7/21 10:09 上午
# script name: apply.py
# usage: task apply program

from proj.tasks import *

re1 = taskA.delay(10, 20)
re2 = taskB.delay(1, 2, 3)
re3 = add.delay(34, 35)

r_list = [re1, re2, re3]
for r in r_list:
    while not r.ready():
        pass
    print(r.result)