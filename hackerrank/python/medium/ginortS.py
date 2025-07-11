def sortingWord(sub_string=""):
    if sub_string.islower():
        return (0, sub_string)

    if sub_string.isupper():
        return (1, sub_string)

    if sub_string.isdigit():
        x = int(sub_string)
        if x % 2 == 1:
            return (2, sub_string)

    return (3, sub_string)


string = input().strip()
print(''.join(sorted(string, key=sortingWord)))
