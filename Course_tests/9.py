def summary_ranges(elements: list) -> list:
    result = []
    ranges = ''

    if not elements:
        return result

    for i, _ in enumerate(elements):
        if i != len(elements)-1:
            if elements[i+1] - elements[i] == 1:
                if elements[i-1] - elements[i] != -1:
                    ranges += str(elements[i])+'->'
            else:
                if elements[i-1] - elements[i] == -1:
                    ranges += str(elements[i])
                    result.append(ranges)
                    ranges = ""
        else:
            if elements[i-1] - elements[i] == -1:
                ranges += str(elements[i])
                result.append(ranges)

            return result


def summary_ranges_example(numbers):
    """
    hexlet example
    """
    if not numbers:
        return []

    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]

    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    # здесь [0, 1, 2, 7, 5, 6] уже преобразован
    # в [[0, 1, 2], [7], [5, 6]]

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append('{}->{}'.format(first, last))

    return ranges


def main():
    print(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]))
    print(summary_ranges([1, 2, 3]))
    print(summary_ranges([]))


if __name__ == '__main__':
    main()
