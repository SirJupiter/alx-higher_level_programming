#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    remove_keys = [i for i, j in a_dictionary.items() if j is value]

    for item, val in a_dictionary.items():
        if item in remove_keys:
            del a_dictionary[item]

    return a_dictionary
