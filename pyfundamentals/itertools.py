from itertools import islice, count


from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


# islice(all_primes,1000)
thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(sum(list(thousand_primes)))

print(any({1,2,3,4,0}))
print(all({1,2,3,4,0}))
print(any(x for x in range(1213,1324) if is_prime(x)))
print(all(n == n.title() for n in {"Abinash","Baba","mama"}))


sunday = [10,11,8,18,12,14,13,11,18]
monday = [21,20,8,11,9,1,9,4,17]
tuesday = [5,8,2,5,11,10,12,2,3]

for temps in zip(sunday,monday,tuesday):
    print('min={:5.2f}, max={:5.2f}, average={:5.3f}'.format(min(temps),max(temps),sum(temps)/len(temps)))

from itertools import chain
temp = chain(sunday, monday, tuesday)

print(all(t > 0 for t in temp))
def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a,b = b, a+b

for x in (p for p in lucas() if is_prime(p)):
    print(x)