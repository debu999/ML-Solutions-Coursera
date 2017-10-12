store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key = last_letter, reverse=True)


print(sort_by_last_letter(["Debabrata", "Priyabrata", "Ramesh", "Devendra", "Augustine", "Boominathan"]))

#Closure testing

def enclosing():
    x,y = 'ABC', 'PQR'


    def inner():
        print(x,y)


    return inner

lf = enclosing()


lf()


print(lf.__closure__)


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

sqrt = raise_to(.5)
sqr = raise_to(2)
print(sqrt)
print(sqrt(4), sqr(4))


#bindings

message = 'Global'

def enclosing():
    message = 'Enclosing'
    def local():
        message = 'local'
        print("local msg:", message)

    print("enclosing msg:", message)
    local()
    print("enclosing msg:", message)

print("Global msg: ", message)
enclosing()

#global and nonlocal usage


import time


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed


timing = make_timer()

print(timing())
time.sleep(2)
print(timing())

def escape_unicode(f):
    def wraps(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wraps


@escape_unicode
def n_city():
    return "Tromsø"

print(n_city())



class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print("Hello {}".format(name))




hello("Debabrata")
hello("Priyu")
hello("Abhijeet")
# print(hello.__closure__)
print(hello.f)
print(hello.count)

#As class instance variable

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:]+[l[0]]
l = [ 1, 2, 3]
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)

tracer.enabled = True

@tracer
@escape_unicode
def new_city_make(name):
    return name+" - Tromsø"

print(new_city_make("Deb"))

@escape_unicode
@tracer
def new_city_make(name):
    return name+" - Tromsø"

print(new_city_make("Deb"))
tracer.enabled = True
class NewCity:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def new_city_make(self, name):
        return name + " looking for a change. - Suffix: "+self.suffix


cty = NewCity("title is Patnaik.")

print(cty.new_city_make("Deb"))
