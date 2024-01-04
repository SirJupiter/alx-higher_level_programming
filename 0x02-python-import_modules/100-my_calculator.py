#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    arg_count = len(argv)

    a = int(argv[1])
    b = int(argv[3])
    operators = ('+', '-', '*', '/')

    if arg_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
