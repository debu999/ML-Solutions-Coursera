import os
import sys
from pprint import pprint as pp

pp(sys.getdefaultencoding())
filenm="ex.txt"
def write_file(filenm):
    try:
        try:
            os.remove(filenm)
            pp("File removed {}/{}".format(os.getcwd(),filenm))
        except:
            pass
        f = open(filenm, mode='at', encoding='utf-8')
        f.write("Text Line 1\nText Line 2\nText Line 3\nText Line 4\nText Line 5")
        f.close()
    except:
        print("File opearation met with error. Check permission to write in directory {}".format(os.getcwd()))
    finally:
        f.close()

def read_file(filenm):
    try:
        f = open(filenm, "rt")
        pp(f.readlines())
    except:
        print("File opearation met with error. Check permission to read from directory {}".format(os.getcwd()))

if __name__ == "__main__":
    write_file(filenm=filenm)
    # read_file(filenm=filenm)
    with open(filenm) as f:
        for ln in iter(lambda: f.readline().strip(), 'Text Line 5'):
            pp(ln)


import datetime
import itertools
import random

import time

class CPUUsage:

    def __iter__(self):
        return self


    def get_cpu_load(self):
        """ Returns a list CPU Loads"""
        result = []
        cmd = "WMIC CPU GET LoadPercentage "
        response = os.popen(cmd + ' 2>&1', 'r').read().strip().split("\n")
        for load in response[2:]:
            result.append(int(load))
        return result

    def __next__(self):
        cpu_load = self.get_cpu_load()
        return "Current CPU LOAD IS : {}".format(cpu_load)



sensor = CPUUsage()

timestamp = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamp, sensor), 100):
    print(stamp, value)
    time.sleep(.5)


