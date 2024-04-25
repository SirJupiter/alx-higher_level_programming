#!/usr/bin/python3
"""Module contains the find_peak function"""


def find_peak(list_of_integers):
    """
    functionfinds a peak in a list of unsorted integers.
    """
    for num in list_of_integers:
        if type(num) is not int:
            return

    if len(list_of_integers) == 0:
        return None

    max_index = 0

    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > list_of_integers[max_index]:
            max_index = i

    return list_of_integers[max_index]
