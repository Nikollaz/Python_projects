import validation_response

def sudoku_validation(matriz):
    """
        Validation of the sudoku values
    """
    sudoku_validation_response = validation_response.validation_response(True, 0)

    for i, val_i in enumerate(matriz):

        row_validation_response = row_validation(val_i)
        sudoku_validation_response.operations += row_validation_response.operations
        #Row validation
        if row_validation_response.status != True:
            sudoku_validation_response.status = False
            break

        column_validation_response = column_validation(matriz, val_i, i)
        sudoku_validation_response.operations += column_validation_response.operations
        #Column validation
        if column_validation_response.status != True:
            sudoku_validation_response.status = False
            break

        cube_validation_response = cube_validation(matriz, i)
        sudoku_validation_response.operations += cube_validation_response.operations
        #Cube validation
        if cube_validation_response.status != True:
            sudoku_validation_response.status = False
            break

    return sudoku_validation_response

def row_validation(row):
    """
        Validation of the values of each row
    """
    new_response = validation_response.validation_response(True, 0)

    for i, val_i in enumerate(row):

        if i != len(row)-1:

            for j, val_j in enumerate(row[i+1:]):

                new_response.operations += 1
                if val_i == val_j:
                    new_response.status = False
                    break

        if new_response.status != True:
            break

    return new_response

def column_validation(matrix, row, row_index):
    """
        Validation of the values of each column
    """
    new_response = validation_response.validation_response(True, 0)

    for i, val_i in enumerate(matrix[row_index+1:]):

        for j, val_j in enumerate(val_i):

            new_response.operations += 1
            if val_j == row[j]:
                new_response.status = False
                break

        if new_response.status != True:
            break

    return new_response

def cube_validation(matrix, row_index):
    """
        Validation of the 3x3 sections
    """

    new_response = validation_response.validation_response(True, 0)

    #Here i control the execution of the 3x3 control so it only executes thrice
    if row_index == 0 or row_index == 3 or row_index == 6:

        column_counter = 0
        row_counter = 0
        new_matrix = []

        if row_index == 0:

            for a in range(row_index, 3):
                new_matrix.append(matrix[a])

        elif row_index == 3:

            for a in range(row_index, 6):
                new_matrix.append(matrix[a])

        elif row_index == 6:

            for a in range(row_index, 9):
                new_matrix.append(matrix[a])

        new_cube_matrix = [
            [
                [new_matrix[0][0], new_matrix[0][1], new_matrix[0][2]],
                [new_matrix[1][0], new_matrix[1][1], new_matrix[1][2]],
                [new_matrix[2][0], new_matrix[2][1], new_matrix[2][2]]
            ],
            [
                [new_matrix[0][3], new_matrix[0][4], new_matrix[0][5]],
                [new_matrix[1][3], new_matrix[1][4], new_matrix[1][5]],
                [new_matrix[2][3], new_matrix[2][4], new_matrix[2][5]]
            ],
            [
                [new_matrix[0][6], new_matrix[0][7], new_matrix[0][8]],
                [new_matrix[1][6], new_matrix[1][7], new_matrix[1][8]],
                [new_matrix[2][6], new_matrix[2][7], new_matrix[2][8]]
            ]
        ]

        for cube in new_cube_matrix:

            for i, val_i in enumerate(cube):
                for j, val_j in enumerate(val_i):

                    #Here i manage the column position so i can avoid the same comparisons already made
                    column_counter = j + 1

                    for k, val_k in enumerate(cube[row_counter:]):
                        for l, val_l in enumerate(val_k[column_counter:]):

                            new_response.operations += 1

                            if (val_j == val_l) and (j != (l + column_counter) or (k + row_counter) != i):

                                new_response.status = False
                                return new_response

                        column_counter = 0

                #Here i manage the row position so i can avoid the same comparisons already made
                if row_counter < 2:
                    row_counter += 1
                elif row_counter == 2:
                    row_counter = 0

    return new_response
