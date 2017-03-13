#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (node id) and 4 (post)
# and split the post into words delimited by special characters.

import sys
import csv
import re
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
        #if line[0] == "id" or line[0] == "user_ptr_id":
        #    continue
        if len(line) == 19:
            author_id = line[3]
            date = line[8]
            try:
                date = datetime.strptime(date[:13], "%Y-%m-%d %H")
            except:
                continue
            
            print "{0}\t{1}".format(author_id, date.hour)

if __name__ == "__main__":
    mapper()


