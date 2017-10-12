import sys

def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria

    Args:
        x: The Number for which square root to be computed.

    Returns:
        The square root of x.

    Raises:
        Value error if x is negative
    """

    if x < 0:
        raise ValueError("Cannot compute square root of a negative number {}".format(x))
    v1 = x
    step = 0

    while v1*v1 != x and step < 20:
        v1 = ( v1 + x / v1 ) / 2.0
        step += 1

    return v1


def main():
    try:
        print(sqrt(9))
        print(sqrt(16))
        print(sqrt(25))
        print(sqrt(-1))
        print("This is never printed as above statement will throw error.")
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")
    except ValueError as err:
        print(err, file=sys.stderr)


    print("Program execution continues normally here")

if __name__ == "__main__":
    main()

