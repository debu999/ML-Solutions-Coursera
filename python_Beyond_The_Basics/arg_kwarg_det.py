"""
*args must be the last on and all other call to function with arg after *args
must be with the name. Same goes to **kwargs it has to be the last one after *args
"""

def trace(f, *args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)
    result = f(*args, **kwargs)
    print("result = ",result)
    return result


print(int("ff", base=16))

print(trace(int, "ff", base=16))

sunday = [15, 1, 12, 7, 7, 12, 10, 12, 13]
monday = [13, 14, 2, 5, 16, 5, 20, 19, 5]
tuesday = [15, 13, 3, 4, 20, 4, 13, 1, 20]
day = (sunday, monday, tuesday)
from pprint import pprint as pp
pp(list(zip(sunday, monday, tuesday)))
pp(list(zip(*day)))