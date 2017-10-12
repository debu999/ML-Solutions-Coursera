a = 23
b = 23

print(id(a) == id(b), id(b), id(a))

p = [1, 3, 5]
q = [1, 3, 5, ]
print(p, q, p == q, q is p, p is q)

import time


def ret_time(tm = time.ctime()):
    """This Function Returns current Time"""
    return time.ctime()


# LEGB LOCAL ENCLOSING GLOBAL BUILTIN its for scope of variables

count = 0

def show_count():
    print("count = ",count)

def set_count(c):
    global count
    count = c