def main():
    t = ([0], [0])
    t = (t[1],) + t
    t[0][0] += 1
    t[1][0] += 2
    t[2][0] += 3
    print(t)


if __name__ == '__main__':
    main()
