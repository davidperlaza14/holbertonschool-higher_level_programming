#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = num = int(repr(number)[-1])
if int(repr(number)[-1]) >= 5:
    print(f"Last digit of {number} is {num} and is greater than 5 ")
elif int(repr(number)[-1]) == 0:
    print(f"Last digit of {number} is {num} and is 0")
else:
    int(repr(number)[-1]) < 6 and 0
    print(f"Last digit of {number} is  {num} and is less than 6 and not 0")