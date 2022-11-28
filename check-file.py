#!/usr/bin/python3
import os
path = '/tmp/testfile.txt'
if os.path.isdir(path):
    print("it is a directory")
elif os.path.isfile(path):
    print("it is a file")
else:
    print("file or directory does not exist.")
