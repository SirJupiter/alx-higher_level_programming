#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for i in matrix:
        for j in range(len(i)):
            if j != i.index(i[-1]):
                print("{:d}".format(i[j]), end=' ')
            else:
                print("{:d}".format(i[j]))
