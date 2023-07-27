def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values for the current row
        squared_row = []
        # Iterate over each element in the current row and square it
        for num in row:
            squared_row.append(num ** 2)
        # Add squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix
