#!/usr/bin/python3
import os
userlist = ["alpha", "beta", "gamma"]

print("Adding system to user")
print("------------------------------------------")

#loop to add user from userlist
for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("user {} does not exist. Addint it.....".format(user))
        print("######################################")
        print()
        os.system("useradd {}".format(user))
    else:
        print("User laready exist. Skipping it.")
        print("######################################")
        print()
