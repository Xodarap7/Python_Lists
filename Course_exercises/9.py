def find_index(find, elements):

    for index, value in enumerate(elements):

        if value == find:
            return index

    else:
        return None


def find_second_index(value, items):
    iterator = iter(items)
    first = find_index(value, iterator)
    second = find_index(value, iterator)

    if second is not None:
        return first + second + 1


def main():
    l = [1, 2, 3, 4]
    s = "Hello world"

    print(find_second_index("l", s))


if __name__ == '__main__':
    main()
