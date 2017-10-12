"""sorted_set Module"""

from collections.abc import Sequence
from collections.abc import Set
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence, Set):
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def _is_sorted_and_unique(self):
        return all(self[i] < self[i+1] for i in range(len(self)-1))

    
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, idx):
        res = self._items[idx]
        return SortedSet(res) if isinstance(idx, slice) else res

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ""
        )

    def __eq__(self, rhs):
        if isinstance(rhs, SortedSet):
            return self._items == rhs._items
        return NotImplemented

    def __ne__(self, rhs):
        if isinstance(rhs, SortedSet):
            return self._items != rhs._items
        return NotImplemented

    def count(self, item):
        return int(item in self)


    def index(self, item):
        idx = bisect_left(self._items, item)
        if (idx != len(self._items)) and (self._items[idx] == item):
            return idx
        raise ValueError("{} not found".format(repr(item)))

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs))

    def __mul__(self, cnt):
        return SortedSet() if cnt<1 else self

    def __rmul__(self, cnt):
        return SortedSet() if cnt<1 else self

    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)



if __name__ == "__main__":
    from random import randrange
    from pprint import pprint as pp
    from timeit import timeit
    s = SortedSet(randrange(1000) for _ in range(2000))
    p = [s.count(i) for i in range(999)]
    pp(len(s))
    pp(timeit(setup="from __main__ import s",
           stmt="[s.count(i) for i in range(999)]",
           number=100))



