#!/usr/bin/python

for i in xrange(100):
    with open('file-%.3d' %i,'w') as fd:
        fd.write('some text \n')
