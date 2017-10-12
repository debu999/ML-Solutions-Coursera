#!/usr/bin/env python

import wordcount

a,b = wordcount.count_words_web("https://www.google.com")
print(len(a),len(b))

t = wordcount.count_words_fl("test1.py")
print(t is None)