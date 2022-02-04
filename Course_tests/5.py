def chunked(size, source):
    result = []
    index = 0

    while index < len(source):
        result.append(source[index:index + size])
        index += size

    return result


def main():
    print(chunked(2, ['a', 'b', 'c', 'd']))
    print(chunked(3, 'foobar'))
    print()


if __name__ == '__main__':
    main()
