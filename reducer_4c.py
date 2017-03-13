#!/usr/bin/python

import sys
import csv
from heapq import *

old_tag = None
count = 0
tag_hq = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    tag, num = data_mapped
    if old_tag and old_tag != tag:
        if len(tag_hq) < 10:
            heappush(tag_hq, (count, tag))
        else:
            heappushpop(tag_hq, (count, tag))
        count = 0
        
    old_tag = tag
    count += int(num)

if len(tag_hq) < 10:
    heappush(tag_hq, (count, tag))
else:
    heappushpop(tag_hq, (count, tag))

result = [heappop(tag_hq) for i in range(len(tag_hq))]

for i in reversed(range(len(result))):
    print "%s\t%d" % (result[i][1], result[i][0])
