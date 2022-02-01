def is_continuous_sequence(elements: list) -> bool:
    current = None

    if len(elements) < 2:
        return False

    for element in elements:
        if current:
            if element - current != 1:
                break
            else:
                current = element
        else:
            current = element
    else:
        return True

    return False


def is_continuous_sequence_example(source):
    if len(source) < 2:
        return False
    for x, y in zip(source, source[1:]):
        if (y - x) != 1:
            return False
    return True


def main():
    test_true = [1, 2, 3, 4, 5]
    test_false = [5, 6, -7, 8]
    print(is_continuous_sequence(test_true))
    print(is_continuous_sequence(test_false))
    print(is_continuous_sequence_example(test_false))


if __name__ == '__main__':
    main()
