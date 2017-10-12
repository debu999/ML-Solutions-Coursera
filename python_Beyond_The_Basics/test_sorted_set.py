import unittest

from pprint import pprint as pp
from collections import (Sized, Container, Iterable, Sequence, Set)
from sorted_set import SortedSet


class TestConstruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([6, 3, 5, 1, 0])

    def test_with_duplicates(self):
        s = SortedSet([2, 2, 3, 2, 3, 2, 3, 1, 3, 2])

    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2

        g = gen6842()
        s = SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()


class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([2, 3, 4, 7, 3, 2, 7, 9, 1])

    def test_positive_contained(self):
        self.assertTrue(3 in self.s)

    def test_negative_contained(self):
        self.assertFalse(19 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(158 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(4 not in self.s)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))


class TestSizedProtocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([2])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_dups(self):
        s = SortedSet([2, 3, 4, 2, 3, 4, 5, 1, 3, 1, 2])
        self.assertEqual(len(s), 5)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([2, 3, 4, 7, 3, 2, 7, 9, 1])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [1, 2, 3, 4, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet({1, 4, 9, 13, 15})

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_end(self):
        # self.assertRaises(IndexError, self.s[5])
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_beginning(self):
        # self.assertRaises(IndexError, self.s[-6])
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet((1, 4, 9)))

    def test_slice_till_end(self):
        self.assertEqual(self.s[3:], SortedSet([15, 13]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[1:2], SortedSet([4]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], SortedSet({1, 4, 9, 13, 15, 1, 9}))

    def test_reveresed(self):
        s = SortedSet({1, 2, 3, 9, 4, 6})
        r = reversed(s)
        self.assertTrue(next(r), 9)
        self.assertTrue(next(r), 6)
        self.assertTrue(next(r), 4)
        self.assertTrue(next(r), 3)
        self.assertTrue(next(r), 2)
        self.assertTrue(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)

    def test_index_positive(self):
        s = SortedSet({1, 2, 3, 9, 4, 6})
        self.assertEqual(s.index(3), 2)

    def test_index_negative(self):
        s = SortedSet({1, 2, 3, 9, 4, 6})
        with self.assertRaises(ValueError):
            s.index(58)

    def test_count_one(self):
        s = SortedSet([1, 2, 3, 4, 5])
        self.assertEqual(s.count(4), 1)

    def test_count_zero(self):
        s = SortedSet([1, 2, 3, 4, 5])
        self.assertEqual(s.count(14), 0)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        s = SortedSet({1, 2, 3})
        y = SortedSet([4, 5, 6])
        self.assertEqual(s + y, SortedSet([1, 3, 2, 4, 6, 5]))

    def test_concatenate_equal(self):
        s = SortedSet({1, 2, 3})
        y = SortedSet([4, 5, 6])
        self.assertEqual(s + s, s)

    def test_concatenate_intersect(self):
        s = SortedSet({1, 2, 3})
        y = SortedSet([4, 5, 6, 3])
        self.assertEqual(s + y, SortedSet([1, 3, 2, 4, 6, 5]))

    def test_repitition_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s * 0, SortedSet())
        self.assertEqual(0 * s, SortedSet())

    def test_rep_nonzero(self):
        s = SortedSet({1, 2, 3})
        y = SortedSet([4, 5, 6])
        self.assertEqual(s * 229, s)
        self.assertEqual(229 * s, s)


class TestReprProtocol(unittest.TestCase):
    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_some(self):
        s = SortedSet({42, 47, 20, 21, 36})
        self.assertEqual(repr(s), "SortedSet([20, 21, 36, 42, 47])")


class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([2, 3, 5, 2, 1]) ==
                        SortedSet([5, 1, 5, 2, 3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([2, 3, 5, 2, 1]) ==
                         SortedSet([2, 92, 5, 2, 1]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([2, 3, 5, 2, 1]) == [1, 2, 3, 5])

    def test_identical(self):
        s = SortedSet([2, 3, 1])
        self.assertTrue(s == s)


class TestInequalityProtocol(unittest.TestCase):
    def test_positive_inequal(self):
        self.assertTrue(SortedSet([2, 3, 5, 2, 1]) !=
                        SortedSet([5, 1, 15, 5, 2, 3]))

    def test_negative_inequal(self):
        self.assertFalse(SortedSet([2, 3, 5, 2, 1]) !=
                         SortedSet([2, 3, 5, 2, 1, 3]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([2, 3, 5, 2, 1]) != [1, 2, 3, 5])

    def test_identical(self):
        s = SortedSet([2, 3, 1])
        self.assertFalse(s != s)


class TestRelationalSetProtocol(unittest.TestCase):
    def test_le_positive(self):
        s = SortedSet([2, 3, 1])
        t = SortedSet([2, 3])
        self.assertFalse(s <= t)

    def test_le_positive(self):
        s = SortedSet([2, 3, 1])
        t = SortedSet([2, 3])
        self.assertTrue(s > t)


class TestSetProtocol(unittest.TestCase):
    def test_is_subclass(self):
        self.assertTrue(issubclass(SortedSet, Set))


if __name__ == "__main__":
    unittest.main()
