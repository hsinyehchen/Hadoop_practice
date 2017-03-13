#!/usr/bin/python

import sys

sumup = 0
num = 0

oldWeekday = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    weekday, sale = data_mapped
    
    if oldWeekday and oldWeekday != weekday:
        print "{0}\t{1}".format(oldWeekday, sumup/num)
        oldWeekday = weekday;
        sumup = 0
        num = 0

    oldWeekday = weekday
    num += 1
    sumup += float(sale)
if oldWeekday != None:
    print oldWeekday, "\t", sumup/num

