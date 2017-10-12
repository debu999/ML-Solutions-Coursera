from pprint import pprint as pp

ls = [i * 2 for i in range(23)]
pp([ls, type(ls), dir(ls)])
ls.append(2342)

pnt = [(x, y) for x in range(5) for y in range(5)]
pp(pnt)

vals = [[y * 3 for y in range(x)] for x in range(19)]
pp(vals)

map1 = map(ord, "The quick brown fox jump over the lazy dog")

pp(map1)
print(' '.join([chr(data) for data in map1]))

value = [(x // (x - y), x, y) for x in range(100) if x % 29 == 0 for y in range(100) if
         x - y != 0 and x > y and y % 29 == 0]
pp(value)

from project.closure_decorators.local_functions import Trace

result = map(Trace()(ord), 'The Quick Brown Fox Jump over the Lazy Dog')
for data in result:
    pp(data)

# pp(' '.join([chr(data) for data in result]))
rng1 = range(12)
rng2 = range(13)
rng3 = range(14)


def pp_range(r1, r2, r3):
    return "{} {} {}".format(r1, r2, r3)


pp(list(map(pp_range, rng1, rng2, rng3)))

import itertools


def pp_range(qty, r1, r2, r3):
    return "{}: {} {} {}".format(qty, r1, r2, r3)


pp(list(map(pp_range, itertools.count(), rng1, rng2, rng3)))

# Comprehension vs maps
t = [str(i) for i in range(5)]
t1 = list(map(str, range(5)))

t2 = (str(i) for i in range(5))
t3 = map(str, range(5))

pp([t, t1, t2, t3])

positive = filter(lambda x: x > 0, [1, -2, -4, 0, 12, 17, 83, 9, -91, -72, 8])
pp([positive, list(positive)])
pp(list(filter(None, [0, None, [], "", [2, 4, 5], "Hello", False, True])))

from functools import reduce

import operator

sm = reduce(operator.add, [2, 3, 6, 8, 90, 93, 43, 763, 93])
pp(sm)


def test_fun_divide(a, b):
    pp("test_fun_divide {} {}".format(a, b))
    if b == 0:
        b = 1
    return (a // b)


div = reduce(test_fun_divide, [200, 2, 10, 2, 5, .5, .25, .26, 3])
pp(div)

# nuances of reduce optional value to use if the list is empty

pp(reduce(operator.add, range(0), 0))
pp(reduce(operator.add, [], 0))
pp(reduce(operator.mul, range(3), 1))
pp(reduce(operator.concat, ["a", "b", "c"], ""))
pp(reduce(operator.concat, [], ""))

from project.pyfundamentals.wordcount import count_words_web

dict_word = count_words_web(
    "https://stackoverflow.com/questions/9135485/how-to-use-pprint-to-print-"+
    "an-object-using-the-built-in-str-self-method")

# pp(dict_word)
# print(dict_word, len(dict_word))

urls = ["https://stackoverflow.com/questions/9135485/how-to-use-pprint-to-print-"+
    "an-object-using-the-built-in-str-self-method",
        "https://stackoverflow.com/questions/9768865/python-nonetype-object-is-not-callable-beginner",
        "http://www.xe.com/currencycharts/?from=SGD&to=INR",
        "https://docs.python.org/3.6/library/operator.html#operator.countOf"
        ]

counts = map(count_words_web, urls)


def com_dict_cnt(d1, d2):
    d_tmp = d1.copy()
    for word, cnt in d2.items():
        d_tmp[word] = d_tmp.get(word, 0) + cnt
    return d_tmp
pt = [d[0] for d in list(counts)]
res = reduce(com_dict_cnt, pt)

for t in pt:
    print("Dict length is: {}".format(len(t)))

print("Combined Length is : {}".format(reduce(operator.add, [len(dct3) for dct3 in pt], 0)))
print("Reduced Length is : {}".format(len(res)))


class ExIterator:
    def __init__(self, data):
        self.index=0
        self.data=data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        result1 = self.data[self.index]
        self.index += 1
        return result1


# eit = ExIterator()
#
# for i in range(26):
#     try:
#         pp(next(eit))
#     except StopIteration:
#         pp("StopIteration exception encountered for index : {}".format(i))
#
# for fl in ExIterator():
#     pp(fl)



class ExIterable:
    def __init__(self):
        self.data = range(25)

    def __iter__(self):
        return ExIterator(self.data)



# eit = ExIterator()
#
# for i in range(26):
#     try:
#         pp(next(eit))
#     except StopIteration:
#         pp("StopIteration exception encountered for index : {}".format(i))
#
# for fl in ExIterable():
#     pp(fl)

# print([i*5 for i in ExIterable()])


class ExAltIterable:
    def __init__(self):
        self.data = range(10)

    def __getitem__(self, idx):
        return self.data[idx]

print([i*5 for i in ExAltIterable()])

import datetime

i = iter(datetime.datetime.now, None)
 