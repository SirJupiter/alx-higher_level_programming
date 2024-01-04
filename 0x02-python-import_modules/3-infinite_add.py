#!/usr/bin/python3
from sys import argv


def main():
    arg_count = len(argv)
    if arg_count < 2:
        print(0)

    elif arg_count == 2:
        print(argv[1])

    else:
        addition = 0
        for i in range(1, arg_count):
            addition += int(argv[i])

        print(addition)


if __name__ == "__main__":
    main()
