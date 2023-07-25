#!/usr/bin/env python3
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments and their values
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(num_args))

for i, arg in enumerate(sys.argv[1:], 1):
    print("{:d}: {}".format(i, arg))
if __name__ == "__main__":
    pass
