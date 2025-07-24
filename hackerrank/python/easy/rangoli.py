def print_rangoli(size):
    if size == 0:
        return
    start = ord('a')
    end = ord('a') + size
    data = list()
    for _ in range(size):
        pattern = chr(start)
        for i in range(1, size):
            pattern += "-" + (chr(start + i) if start + i < end else "-")

        main_pattern = pattern[:0:-1] + pattern
        data.append(main_pattern)
        start += 1
    if len(data) > 1:
        print(*data[:0:-1], sep="\n")
    print(*data, sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
