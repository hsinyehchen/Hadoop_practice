#!/usr/bin/python

import sys

sumup = 0
count = 0

oldWeekday = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    weekday, sale, num = data_mapped
    
    if oldWeekday and oldWeekday != weekday:
        print "{0}\t{1}\t{2}".format(oldWeekday, sumup/count, count)
        oldWeekday = weekday;
        sumup = 0
        count = 0

    oldWeekday = weekday
    count += int(num)
    sumup += float(sale)*int(num)

if oldWeekday != None:
    print "{0}\t{1}\t{2}".format(oldWeekday, sumup/count, count)

