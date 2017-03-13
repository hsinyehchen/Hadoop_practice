#!/usr/bin/python

import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for data in reader:
    try:
        tmp = int(data[0])
    except:
        continue
    id = data[0]
    type = data[5]
    abs_parent_id = data[7]
    author_id = data[3]
    if type == "question":
        print id+"\t"+author_id
    else:
        print abs_parent_id+"\t"+author_id
     

