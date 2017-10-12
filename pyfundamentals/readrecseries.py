"""Read and print a Recaman's Number Series"""

import sys
from pprint import pprint as pp


def read_series(filename):
    try:
        f = open(filename, mode="rt", encoding="utf-8")
        return [int(ln.strip().strip("'")) for ln in f]
        #
        # series = []
        # for line in f:
        #     a = int(line.strip())
        #     series.append(a)
    finally:
        f.close()

    # return series


def main(filename):
    series = read_series(filename)
    pp(series)


if __name__ == "__main__":
    main(sys.argv[1])