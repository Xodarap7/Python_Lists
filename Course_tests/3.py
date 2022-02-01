def enlarge(image: list) -> list:
    enlarge_list = []

    for line in image:
        enlarge_line = []

        for symbol in line:
            enlarge_line.extend([symbol, symbol])

        enlarge_line = "".join(enlarge_line)
        enlarge_list.extend([enlarge_line, enlarge_line])

    return enlarge_list


def show(image):
    for line in image:
        print(line)


def main():
    frame = [
        '****',
        '*  *',
        '*  *',
        '****'
    ]
    show(enlarge(frame))


if __name__ == '__main__':
    main()
