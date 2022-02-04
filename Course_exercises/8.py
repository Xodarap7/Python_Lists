def find_index(find, elements):

    for index, value in enumerate(elements):

        if value == find:
            return index

    else:
        return None


def main():
    l = [1, 2, 3, 4]
    s = "Hello world"

    print(find_index("r", s))


if __name__ == '__main__':
    main()
