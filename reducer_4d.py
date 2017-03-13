#!/usr/bin/python

import sys

old_id = None
lst_author = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    id, author = data_mapped
    if old_id and old_id != id:
        print old_id+"\t["+",".join(lst_author)+"]"
        lst_author = []
 
    old_id = id
    if not author in lst_author:
        lst_author.append(author)

print old_id+"\t["+",".join(lst_author)+"]"
