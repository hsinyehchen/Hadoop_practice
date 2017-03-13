#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import re

split_str = ' |\n|\\.|\\,|\\!|\\?|\\:|\\;|\\"|\\(|\\)|\\<|\\>|\\[|\\]|\\#|\\$|\\=|\\-|\\/'   
#  .,!?:;"()<>[]#$=-/'
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    
    for line in reader:
        id = line[0]
        body = re.split(split_str, line[4])
        for w in body:
            if len(w) > 0:
                print "{1}\t{0}".format(id, w.lower())

test = 'a. a, a\n a# a! a? a: a; a" a( a) a< a> a[ a] a# a$ a= a- a/'

if __name__ == "__main__":
    mapper()
    #print test
    #a = re.split(split_str, test)
    #print a[1], "len = ", len(a[1])


