#!/usr/bin/python
f=open('/tmp/passwd')
for line in reversed(list(f)):
    print(line)
