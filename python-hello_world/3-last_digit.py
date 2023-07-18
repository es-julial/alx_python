#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
print("Last digit of", number, "is", end=" ")
if Last_digit > 5 and number > 0:
    print(Last_digit, "and is greater than 5", end="\n")
elif Last_digit == 0:
    print(Last_digit, "and is 0", end="\n")
else:
    if number > 0:
        print(Last_digit, "and is less than 6 and not 0", end="\n")
    else:
        print(-Last_digit, "and is less than 6 and not 0", end="\n")