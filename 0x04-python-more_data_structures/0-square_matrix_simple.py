#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    nm = []
    for i in range(len(matrix)):
        nm.append(matrix[i].copy())
        for j in range(len(nm[i])):
            nm[i][j] = nm[i][j] ** 2
    return(nm)
