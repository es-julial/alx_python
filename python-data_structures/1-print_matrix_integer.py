
def print_matrix_integer(matrix=[[]]):
    if not matrix or not any(matrix):
        print()
        return

    for row in matrix:
        for i, num in enumerate(row):
            # Use str.format() to print integers without casting them to strings
            end_char = "\n" if i == len(row) - 1 else " "
            print("{:d}".format(num), end=end_char)
