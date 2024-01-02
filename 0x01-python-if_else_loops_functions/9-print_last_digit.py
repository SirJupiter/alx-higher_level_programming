#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    if number < 0:
        digit = -(digit)
    print(digit, end='')
    return (digit)
