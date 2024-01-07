#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []

    i = 0
    while i < len(my_list):
        new_list.append(my_list[i] % 2 == 0)
        i += 1

    return new_list
