#!/usr/bin/python

import sys
import csv

data_A = None

reader = csv.reader(sys.stdin, delimiter='\t')

for data_mapped in reader:
    #data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6 and len(data_mapped) != 20:
        # Something has gone wrong. Skip this line.
        continue
    #print data_mapped
    type = data_mapped[1]
    
    if type == "A":
        data_mapped.pop(1)
        data_A = data_mapped
    elif type == "B":
        if data_A is None:
            raise ValueError('The data_A should not be None when recv. type B')
        elif data_A[0] != data_mapped[0]:
            raise ValueError('User id mismatch!!!')
        else:
            data_mapped.pop(0)
            data_mapped.pop(1)
            print data_A + data_mapped

    else:
        raise ValueError('Wrong type!!!')
