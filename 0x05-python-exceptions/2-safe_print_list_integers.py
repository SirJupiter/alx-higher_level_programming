#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count, p = 0, 0

    for i in range(x):
        count += 1
        try:
            if count <= x:
                print("{:d}".format(my_list[i]), end='')
                p += 1
        except (ValueError, TypeError):
            pass

    print()

    return p
