"""Callable objects in Python
1. Functions
2. lamba Functions
3. Class since there is constructor
4. Class Functions
5. Call Objects with __call__() implementation
"""

"""Many others are not callable
1. Integer Instance
2. String Instance
3. Objects with no __call__() function in class etc."""

def a():
    return"a"


print(callable(a))


b = lambda b : "b"
print(callable(b))

print(callable(tuple))
print(callable(tuple.count))

class abc:
    def __call__(self):
        print("abc called")

ABC = abc()

print(callable(ABC))

print(callable("My Name is Debabrata"))