def unique_sequence_length(string):
    unique_sequence = set()
    length = 0
    for char in string:
        if char in unique_sequence:
            break
        unique_sequence.add(char)
        length += 1
    return length


def find_longest_length(string):
    longest_length = 0
    for i, _ in enumerate(string):
        substring_length = unique_sequence_length(string[i:])
        if longest_length < substring_length:
            longest_length = substring_length
    return longest_length


def main():
    test_1 = 'abcdeef'
    test_2 = 'qweqrty'
    print(find_longest_length(test_2))
    # print(find_longest_length(test_1))


if __name__ == '__main__':
    main()
