#!/usr/bin/python

import sys
import csv

old_id = None
q_len = 0
a_len_sum = 0
count = 0
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    id, type, length = data_mapped
    if old_id and old_id != id:
        if count == 0:
            avg = 0
        else:
            avg = a_len_sum/count 
        print "{0}\t{1}\t{2}".format(old_id, q_len, avg)
        count = 0
        q_len  = 0
        a_len_sum = 0 
    old_id = id
    if type == "A":
        q_len = int(length)
    elif type == "B":
        count += 1
        a_len_sum += int(length)
    
print "{0}\t{1}\t{2}".format(old_id, q_len, a_len_sum/count)
