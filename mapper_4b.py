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
        id = line[0]
        body = line[4]
        node_type = line[5]
        abs_parent_id = line[7]
        if node_type == "question":
            print "\t".join([id, "A", str(len(body))])
        elif node_type == "answer":
            print "\t".join([abs_parent_id, "B", str(len(body))])
        else:
            continue
        #print "{0}\t{1}".format(author_id, date.hour)

if __name__ == "__main__":
    mapper()


