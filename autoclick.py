# install python 2.7
# pip install pymouse
# pip install pyhook, from http://www.lfd.uci.edu/~gohlke/pythonlibs/
# pip install pyuserinput
# pip install pypiwin32

from pymouse import PyMouse
import time

m = PyMouse()

# a = m.position()
# print(a)

m.move(355, 503)

# a = m.position()
# print(a)

cnt = 0

while True:
    cnt += 1
    print(cnt)
    m.click(355, 503)

    for i in range(44, 0, -1):
        time.sleep(1)
        print("."),
    