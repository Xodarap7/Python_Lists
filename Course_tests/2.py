def triangle(rows: int) -> list:
    row = [1]

    for i in range(rows):
        row.append(row[i] * ((rows - i) / (i + 1)))
    return row


def main():
    print(triangle(2))


if __name__ == '__main__':
    main()
