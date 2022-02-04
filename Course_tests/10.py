def transposed_example(matrix):
    """
    hexlet example
    """
    return list(map(list, zip(*matrix)))


def transposed(matrix):
    transpose = []
    rows = len(matrix[0])

    for column in range(rows):
        transposed_row = []

        for row in matrix:
            transposed_row.append(row[column])
        transpose.append(transposed_row)

    return transpose


def main():
    print(transposed([[1, 2], [3, 4], [5, 6]]))
    print(transposed([[1, 2], [3, 4]]))
    print(transposed([[1]]))


if __name__ == '__main__':
    main()
