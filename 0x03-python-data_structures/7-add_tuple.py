#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        c_a = (0, 0)
    elif len(tuple_a) == 1:
        c_a = (tuple_a[0], 0)
    else:
        c_a = tuple_a

    if len(tuple_b) == 0:
        c_b = (0, 0)
    elif len(tuple_b) == 1:
        c_b = (tuple_b[0], 0)
    else:
        c_b = tuple_b

    new_tuple = (c_a[0] + c_b[0], c_a[1] + c_b[1])

    return new_tuple
