def duplicate(l: list):
    l.extend(l)


def main():
    l = [1, 2]
    print(duplicate(l))
    print(l)


if __name__ == '__main__':
    main()
