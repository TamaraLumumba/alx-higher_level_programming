#!/usr/bin/python3

for i in range(122, 96, -1):
    print("{:c}".format(i), end="")
    i -= 32
    print("{:c}".format(i), end="")
    print(" ")