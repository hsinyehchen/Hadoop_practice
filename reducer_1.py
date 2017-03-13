#!/usr/bin/python

import sys

wordTotal = 0
oldWord = None
id_list = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, id = data_mapped
    
    if oldWord and oldWord != thisWord:
        print "{0}\t{1}\t{2}".format(oldWord, wordTotal, id_list)
        oldWord = thisWord;
        wordTotal = 0
        id_list = []

    oldWord = thisWord
    wordTotal += 1
    id_list.append(id)
if oldWord != None:
    print oldWord, "\t", wordTotal

