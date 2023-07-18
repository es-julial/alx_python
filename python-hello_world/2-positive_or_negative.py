#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number), end="\n")
elif number == 0:
    print("{:d} is zero".format(number), end="\n")
else:
    print("{:d} is negative".format(number), end="\n")