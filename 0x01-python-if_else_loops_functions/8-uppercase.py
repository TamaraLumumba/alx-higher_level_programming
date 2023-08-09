#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if 'a' <= c <= 'z':
            upper_ascii = ord(c) - 32  # Convert lowercase ASCII to uppercase ASCII
            print("{:c}".format(upper_ascii), end="")
        else:
            print(c, end="")
    print()  # Print a new line at the end
