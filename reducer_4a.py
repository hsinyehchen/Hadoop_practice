#!/usr/bin/python

import sys
import csv

old_id = None
count_hour = [0]*24
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    id, hour = data_mapped
    if old_id and old_id != id:
        m = max(count_hour)
        idx = [str(i) for i in range(len(count_hour)) if count_hour[i] == m]
        print id + "\t" + " ".join(idx)
        count_hour = [0]*24 
    old_id = id
    count_hour[int(hour)] += 1



m = max(count_hour)
idx = [str(i) for i in range(len(count_hour)) if count_hour[i] == m]
print id + "\t" + " ".join(idx)

