from math import sqrt


def get_square_roots(number: int) -> list:
    roots = []

    if number >= 0:

        if number != 0:
            roots.append(-sqrt(number))

        roots.append(sqrt(number))

    return roots


def get_range(number: int) -> list:
    range_list = []
    i = 0

    while number > i:
        range_list.append(i)
        i += 1

    return range_list


def main():
    roots = get_square_roots(-81)
    print(roots)
    range_list = get_range(5)
    print(range_list)


if __name__ == '__main__':
    main()
