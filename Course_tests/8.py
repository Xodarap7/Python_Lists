def compare_version(v1: str, v2: str) -> int:
    v1 = v1.split('.')
    v2 = v2.split('.')
    print(v1, v2)

    for ver1, ver2 in zip(v1, v2):
        ver1 = int(ver1)
        ver2 = int(ver2)
        if ver1 == ver2:
            continue
        elif ver1 > ver2:
            return 1
        elif ver2 > ver1:
            return -1
    else:
        return 0


def main():

    print(compare_version('0.2', '0.12'))


if __name__ == '__main__':
    main()
