import math

print(math.factorial(32))

n=7
k=3
t = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(t)

from math import factorial as fct

t=fct(n) // (fct(k)*fct(n-k))

print(t)

# print(len(str(fct(90000))))

print(10)
print(0b10)
print(0o10)
print(0x12)

print(int(23.8))
print(int("23423"))
print(int("23423", 5))

print(float("3e52"))
print(float("1.6522e-12"))
print(float("inf"))
print(float("-inf"))
print(float("nan"))

print("None: "+ str(None))
a = None
print(str(a is None))

