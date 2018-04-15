#!/usr/bin/env python
#coding:utf-8

'makeTextFile.py -- create text file'

import os
ls = os.linesep

#get filename
fname = "fname"
while True:
    if os.path.exists(fname):
        print("ERROR:'%s' already exists" % fname )
    else:
        break

all = []
print("\nEnter Lines ('.' by itself to quit).\n")

while True:
    entry = input('> ')
    if entry == '.':
        break;
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print("DONE!")
