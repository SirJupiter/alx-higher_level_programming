#!/usr/bin/python3

def uniq_add(my_list=[]):
    addition = 0
    for item in set(my_list):
        addition += item

    return addition
