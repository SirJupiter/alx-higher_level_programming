#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    if number < 0:
        digit = -1 * digit
    print("{:d}".format(digit), end='')
    return (digit)
