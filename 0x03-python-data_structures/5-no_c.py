#!/usr/bin/python3

def no_c(my_string):
    new = ""
    new.join(chr for char in my_string if char.lower() not in {'c'})
    return (new)
