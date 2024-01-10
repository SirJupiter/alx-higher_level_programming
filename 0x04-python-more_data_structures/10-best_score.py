#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    highest = 0
    for key in a_dictionary:
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]

    for key in a_dictionary:
        value = a_dictionary[key]
        if value is highest:
            return key
