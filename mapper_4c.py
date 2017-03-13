#!/usr/bin/python

import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    tag = line[2].split()
    for t in tag:
        print "%s\t1" % t
    

