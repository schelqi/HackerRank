
def sorting_word(sub_string=""):
    # All sorted lowercase letters are ahead of uppercase letters.
    if sub_string.islower():
        return 0, sub_string

    # All sorted uppercase letters are ahead of digits.
    if sub_string.isupper():
        return 1, sub_string

    # All sorted odd digits are ahead of sorted even digits.
    if sub_string.isdigit():
        x = int(sub_string)
        if x % 2 == 1:
            return 2, sub_string

    return 3, sub_string

if __name__ == '__main__':
    string = input().strip()
    print(''.join(sorted(string, key=sorting_word)))
