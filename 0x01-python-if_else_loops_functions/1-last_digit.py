#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = int((str(number))[-1])
else:
    last_digit = int((str(number))[-1]) * -1
if last_digit > 5:
    post = "and is greater than 5"
if last_digit == 0:
    post = "and is 0"
if last_digit < 6 and last_digit != 0:
    post = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {post}")
