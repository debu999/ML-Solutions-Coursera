#!/usr/bin/env python
"""
Word Count Module provides option to analyse words in files or URL.

There are 2 functions count_words_fi and count_words_web

USAGE:
    count_words_fl(<<FILE NAME>>)

    count_words_web(<<URL PATH>>)
"""

import sys
from urllib.request import urlopen


def count_words_fl(filename):
    """
    Read a file passed as parameter.
    Store the word in a dictionary with the count.
    Print the words and their count in sorted order.

    Args: File Name which has to be analysed

    Returns: None
    """

    result = dict()
    with open(filename,'r') as fl:
        for ln in fl:
            for word in ln.split():
                result[word] = result.setdefault(word, 0)+1

    for word, count in sorted(result.items(),key=lambda x:x[1]):
        print("{} {}".format(word, count))


def count_words_web(url):
    """
    Read a url passed as parameter.
    Store the word in a dictionary with the count and store all words in a list.
    Return the list and dictionary to calling process.

    Args: URL which has to be analysed

    Returns: A Dictionary and a List
    """

    with urlopen(url) as webdata:
        webwordlist = []
        webworddict = {}
        for line in webdata:
            line_words =  line.decode("utf-8", errors='ignore').split()
            for word in line_words:
                webwordlist.append(word)
                webworddict[word] = webworddict.setdefault(word,0)+1

    # print(len(webworddict))
    # print(len(webwordlist))
    return(webworddict,webwordlist)

if __name__ == "__main__":
    count_words_fl(sys.argv[1])