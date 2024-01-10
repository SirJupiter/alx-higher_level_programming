#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    remove_keys = [i for i, j in a_dictionary.items() if j is value]

    for t in remove_keys:
        del a_dictionary[t]

    return a_dictionary
