#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    # Start from index 1 to exclude script name from arguments
    for arg in argv[1:]:
        total += int(arg)
    print(total)
