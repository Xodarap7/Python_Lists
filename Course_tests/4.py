def length_of_last_word(element: str) -> int:
    words = element.split()
    if not words:
        return 0
    return len(words[-1])


def main():
    print(length_of_last_word('man in Black'))
    print(length_of_last_word('hello\t\nworld'))
    print(length_of_last_word(''))


if __name__ == '__main__':
    main()
