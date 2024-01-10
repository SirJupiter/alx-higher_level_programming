#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    num_before = 0

    for char in reversed(roman_string):
        if romans[char] < num_before:
            num = num - romans[char]
        else:
            num = num + romans[char]
        num_before = romans[char]

    return num
