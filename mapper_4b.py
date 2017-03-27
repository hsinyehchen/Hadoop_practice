#!/usr/bin/python

import sys
import csv
import re
from datetime import datetime

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


