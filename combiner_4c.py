#!/usr/bin/python

import sys
import csv

old_tag = None
count = 0
tag_heapq = []

class MyTag:
    """ Class for tag and count and comparator """
    tag = ""
    count = 0
    def __init__(self, tag, count):
        self.tag = tag
        self.count = count
    def __cmp__(self, other):
        return cmp(self.count, other.count)


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    tag, num = data_mapped
    if old_tag and old_tag != tag:
        print "%s\t%d" % (tag, count)
        count = 0
        
    old_tag = tag
    count += int(num)

print "%s\t%d" % (tag, count)

