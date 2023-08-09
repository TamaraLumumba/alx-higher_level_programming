#!/usr/bin/python3

for i in range(122, 96, -1):
print("{:c}".format(i), end="")
    if i != 90:  # 'Z' should be printed only once
        i -= 32
        print("{:c}".format(i), end="")
        print(" ")
