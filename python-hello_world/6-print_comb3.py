#!/usr/bin/python3
for i in range(100):
    for x in range(i+1, 10):
        if i == 8 and x == 9:
            print("{:d}{:d}".format(i, x), end="\n")
        else:    
            print("{:d}{:d},".format(i, x), end=" ")
