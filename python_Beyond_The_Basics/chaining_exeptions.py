from pprint import pprint as pp
import math
import traceback

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    return math.degrees(math.atan(dy/dx))

if __name__ == "__main__":
    pp(inclination(3, 5))
    try:
        pp(inclination(0, 2))
    except ZeroDivisionError as z:
        try:
            raise InclinationError("Slope cannot be vertical") from z
        except InclinationError as ierr:
            pp(ierr)
            pp(ierr.__cause__)
            pp(str(ierr.__cause__))
            pp(ierr.__traceback__)
            traceback.print_tb(ierr.__traceback__)
            tb = traceback.format_tb(ierr.__traceback__)
            pp(tb)
    finally:
        pp("Its completed processing")


    assert True, "No issue occured"
    try:
        assert False, "Checking Assertion "
    except AssertionError as a:
        pp("trapped assertion Error")