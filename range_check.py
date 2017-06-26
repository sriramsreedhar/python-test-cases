#!/usr/bin/python

def range_check(num,start,stop):
    if num in range(start,stop):
       print "%s is within range" %str(num) 
    else:
       print "The number %s is outside range" %str(num)


range_check(10,2,22)

