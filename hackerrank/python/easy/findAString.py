def count_substring(string, sub_string):
    start = 0
    count = 0
    while string.find(sub_string, start) != -1:
        count += 1
        start = string.find(sub_string, start) + 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))
