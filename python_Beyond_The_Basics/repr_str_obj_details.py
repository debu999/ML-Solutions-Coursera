
import random

class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return ("({} {})".format(self._x, self._y))


    def __repr__(self):
        return ("Point2D(x={}, y={})".format(self._x, self._y))


    def __format__(self, f):
        # return "[Formatted point: {} {} {}]".format(self._x, self._y, f)
        if f != "r":
            return "{} {}".format(self._x, self._y)
        else:
            return "{} {}".format(self._y, self._x)
p1 = Point2D(1,2)
from pprint import pprint as pp

pp(str(p1))
pp(repr(p1))
p2 = repr(p1)
pp(type(p2))

####__str__ if not defined calls __repr__ for the class/object

l = [Point2D(i, j) for i,j in zip(range(12), [k*3/2 for k in range(12)])]
for i in range(len(l)):
    print(l[i])

print(l)
print("{:r}".format(Point2D(1,2))) # uses str function to print based on func implementation
print("{!r}".format(Point2D(23, 91))) # forces repr if !r is used

print("{!s}".format(Point2D(23, 91))) # forces str if !s is used
a = random.randrange(0,100,1)
points = [Point2D(x, y) for x in range(10) for y in [ y * random.randrange(0,100,1) for y in range(10)]]
pp(len(points))

import reprlib
pp(reprlib.repr(points))

pp(chr(147))
chr_cd = chr(190)
pp(ord(chr_cd))

text = "Debabrata"

for ch in text:
    print(ch, end=" ")
print("")
for ch in text:
    print(ord(ch), end=" ")
print("")
for ch in text:
    print(ascii(ch), end=" ")

print("")
for ch in text:
    print(chr(ord(ch)), end=" ")