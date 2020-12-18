#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    nm = []
    for i in range(len(matrix)):
        nm.append(list(map(lambda x: x * x, matrix[i])))
    return(nm)
