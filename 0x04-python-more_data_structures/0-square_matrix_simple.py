#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []

    for row in matrix:
        my_matrix.append(list(map(lambda x: x**2, row)))
    return my_matrix
