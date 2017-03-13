#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (node id) and 4 (post)
# and split the post into words delimited by special characters.

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in reader:
        if line[0] == "id" or line[0] == "user_ptr_id":
            continue
        if len(line) == 5:
            line.insert(1, "A")
            writer.writerow(line)
        elif len(line) == 19:
            line.insert(0, line[3])
            line.insert(1, "B")
            line.pop(5)
            writer.writerow(line)

if __name__ == "__main__":
    mapper()


