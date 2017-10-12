from pprint import pprint as pp
class Base:
    def __init__(self):
        pp("Base Initializer")


    def f(self):
        pp("In Base.f()")



class Sub(Base):
    def __init__(self):
        super().__init__()
        pp("Sub Initializer")


    def f(self):
        pp("In Sub.f()")


b = Base()
s = Sub()

b.f()
s.f()

class SimpleList:
    def __init__(self, items):
        self._items = list(items)


    def add(self, item):
        self._items.append(item)


    def __getitem__(self, idx):
        return self._items[idx]


    def sort(self):
        self._items.sort()


    def __len__(self):
        return len(self._items)


    def __repr__(self):
        return "SimpleList{!r}".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()


    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList{!r}".format(list(self))


sl = SortedList([4, 7, 1, -2, 3.92, 72, -820, 92])
sl.add(32)
pp([sl, len(sl), sl._items ])


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports Integer values. {} is not a integer.".format(x))

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList{!r}".format(list(self))

try:
    il = IntList([1, 2, 0, -2, -93])
    pp(il)
    il.add("dslf")
except Exception as e:
    pp(e)


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList {!r}".format(list(self))



sil = SortedIntList([1, 2, 0, -2, -93])
pp([sil])
try:
    sil.add("Debabrata")
except Exception as e:
    print(e)