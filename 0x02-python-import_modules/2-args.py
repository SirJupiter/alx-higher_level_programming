#!/usr/bin/python3
import sys

count = 0
for arg in sys.argv:
    count = count + 1

if count == 1:
    print("0 arguments.")
elif count > 1:
    if count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
