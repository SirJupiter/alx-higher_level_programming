#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_sum = 0
    for tup in my_list:
        weight_sum += tup[1]

    mul_row = 1
    sum_column = 0

    for item in my_list:
        for num in item:
            mul_row *= num
        sum_column += mul_row
        mul_row = 1

    average = sum_column / weight_sum

    return average
