def rotated_left(element):

    if len(element) > 0:
        return element[1:] + element[0:1]


def rotated_right(element):

    if len(element) > 0:
        return element[-1:] + element[:-1]


def main():
    l = [1, 2, 3, 4]
    rotated_left(l)
    rotated_right(l)

    s = "Hello world"
    rotated_left(s)
    rotated_right(s)


if __name__ == '__main__':
    main()
