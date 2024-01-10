#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    total = []
    for i in range(len(matrix)):
        row = [x ** 2 for x in matrix[i]]
        total.append(row)

    return total
