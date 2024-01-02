#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end_digit = number % 10
if number < 0:
    end_digit = -end_digit

if end_digit > 5:
    print(f"Last digit of {number:d} is {end_digit:d} and is greater than 5")
elif end_digit < 6 and end_digit != 0:
    print(f"Last digit of {number:d} is {end_digit:d} and is less "
          f"than 6 and not 0")
else:
    print(f"Last digit of {number:d} is 0 and is 0")
