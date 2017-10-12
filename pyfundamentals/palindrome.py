import unittest




def digits(x):
    """Convert and integer into a list of digits

    Args:
    x : The number to be converted to list of digits.

    Returns:
          A list of digits , in order of ``x``.

    >>> digits(45612356)
    [4, 5, 6, 1, 2, 3, 5, 6]
    """
    # import pdb
    # pdb.set_trace()

    digit_list = []
    while x != 0:
        div, mod = divmod(x, 10)
        digit_list.append(mod)
        x = div

    return digit_list

def is_palindrome(x):
    diglst =  digits(x)
    for f, r in zip(diglst, reversed(diglst)):
        if f != r:
            return False

    return True

class Tests(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(is_palindrome(25111))


    def test_positive(self):
        self.assertTrue(is_palindrome(123454321))


    def test_single_digit(self):
        for i in range(10):
            self.assertTrue(is_palindrome(i))


if __name__ == "__main__":
    unittest.main()
