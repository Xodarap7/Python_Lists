def hamming_weight(number: int) -> int:
    bin_number = bin(number)
    return bin_number.count('1')


def main():
    print(hamming_weight(101))
    print(hamming_weight(4))
    print(hamming_weight(0))


if __name__ == '__main__':
    main()
