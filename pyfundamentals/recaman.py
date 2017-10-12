""""""
import sys
from pprint import pprint as pp

from itertools import count, islice


def sequence():
    "Generate Recaman's Sequence"

    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0  or c in seen:
            c = a + n
        a = c

def write_seq(filenm, num):
    "Write Recaman's Sequence to give filename"
    try:
        f = open(filenm, mode='wt', encoding="utf-8")
        f.writelines("{0}\n".format(rnum)
                     for rnum in islice(sequence(), num + 1))
        f.close()
    except Exception as err:
        print("Error generation Recaman's number and writing to file")
        pp(err)

    finally:
        f.close()


if __name__ == "__main__":
    write_seq(filenm=sys.argv[1], num=int(sys.argv[2]))