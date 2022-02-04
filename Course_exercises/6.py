def rotate(l: list):

    if len(l) > 0:
        l.insert(0, l.pop())


def main():
    l = [1, 2, 3, 4]
    rotate(l)
    print(l)


if __name__ == '__main__':
    main()
