#!/usr/bin/python3
import os

exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group science does not exist. Addintg it >>")
    print("-------------------------------------------")
    print()
    os.system("groupadd science")
    print("Group addded succesfully")
else:
    print("Group already exist")
    print("-------------------------------------------")
    print()
