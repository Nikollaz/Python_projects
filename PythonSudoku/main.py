#!/usr/bin/python
"""
    Basic Python Sudoku validator algorithm

    @author: Nicolas.Saavedra
"""
#pylint: disable-msg=C0103

from classes.sudoku_utils import sudoku_validation

if __name__ == "__main__":

    sudoku_invalid_solution = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    sudoku_valid_solution = [
        [1, 4, 5, 6, 3, 7, 9, 8, 2],
        [6, 2, 9, 4, 1, 8, 3, 7, 5],
        [8, 3, 7, 9, 2, 5, 4, 1, 6],
        [3, 7, 8, 2, 5, 6, 1, 4, 9],
        [9, 6, 4, 8, 7, 1, 5, 2, 3],
        [5, 1, 2, 3, 9, 4, 7, 6, 8],
        [4, 8, 1, 5, 6, 9, 2, 3, 7],
        [7, 5, 3, 1, 8, 2, 6, 9, 4],
        [2, 9, 6, 7, 4, 3, 8, 5, 1]
    ]
    #You can put any example in this function to check the result
    response = sudoku_validation(sudoku_valid_solution)

    if response.status:
        print "Sudoku won, operations: " + str(response.operations)
    else:
        print "Sudoku not won, operations: " + str(response.operations)
