import random
number = random.randint(-10000, 10000)
last = number % 10
s_num = "Last digit of"
fi_ve = "and is greater than 5"
six_zero = "and is less than 6 and not 0"
if (last > 5):
    print(f"{s_num} {number} is {last} {fi_ve}")
elif (last == 0):
    print(s_num + " {} is {} and is 0".format(str(number), str(last)))
elif (last < 6 and last != 0):
    last = abs(number) % 10
    neg_last = -last
    print(f"{s_num} {number} is {neg_last} {six_zero}")
    