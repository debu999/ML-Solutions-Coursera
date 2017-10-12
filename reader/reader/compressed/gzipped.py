import gzip
import sys

opener = gzip.open

if __name__ == '__main__':
    fl = gzip.open(sys.argv[1], mode="wt")
    fl.write(''.join(sys.argv[2:]))
    fl.close()
