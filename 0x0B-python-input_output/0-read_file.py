#!/usr/bin/python3
"""Read a text file and print it to STDOUT"""

def read_file(filename=""):
    """Read file"""
    with open(filename, "r"encoding=ütf-8") as file:
        for line in file:
            print(line, end="")
