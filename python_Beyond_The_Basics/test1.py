import urllib
import urllib.request
print(type(urllib))
# <class 'module'>
print(type(urllib.request))
# <class 'module'>
print(urllib.__path__)
#['C:\\Users\\debab\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\urllib']
try:
    print(urllib.request.__path__)
except:
    pass
"""Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: module 'urllib.request' has no attribute '__path__'"""
print(urllib.request.__file__)
# 'C:\\Users\\debab\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\urllib\\request.py'

import sys
from pprint import pprint as pp
# pp(sys.path)
# pp(sys.path[0])
# pp(sys.path[-5:])

