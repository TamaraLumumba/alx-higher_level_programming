#!/usr/bin/python3

import sys

def main(argv):
    num_args = len(argv)

    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        print("Number of argument(s): {}.".format(num_args))
        print("Argument{}:".format("s" if num_args > 1 else ""), end="\n\n")

        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))

if __name__ == '__main__':
    main(sys.argv[1:])

