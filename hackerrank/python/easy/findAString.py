def count_substring(string, sub_string):
    start = 0
    count = 0

    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        start += 1
        count += 1

    return count


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    print(count_substring(string, sub_string))
