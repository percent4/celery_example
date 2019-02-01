from proj.tasks import add
import time

t1 = time.time()

r1 = add.delay(1, 2)
r2 = add.delay(2, 4)
r3 = add.delay(3, 6)
r4 = add.delay(4, 8)
r5 = add.delay(5, 10)
r6 = add.delay(11, 12)
r7 = add.delay(12, 14)
r8 = add.delay(13, 16)
r9 = add.delay(14, 18)
r10 = add.delay(15, 20)

r_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
for r in r_list:
    while not r.ready():
        pass
    print(r.result)

t2 = time.time()

print(t2-t1)

