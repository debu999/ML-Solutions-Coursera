import bz2
import sys

opener = bz2.open

if __name__ == '__main__':
    fl = bz2.open(sys.argv[1], mode="wt")
    fl.write(''.join(sys.argv[2:]))
    fl.close()
