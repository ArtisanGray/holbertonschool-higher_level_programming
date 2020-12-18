#!/usr/bin/python
def sq(x):
	return(x * x)

def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    nm = []
    for i in range(len(matrix)):
        nm.append(list(map(sq, matrix[i])))
    return(nm)
