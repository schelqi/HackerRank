import itertools

word = input().strip()
word_group_by = itertools.groupby(word)

for key, group in word_group_by:
    letter_count = len(list(group))
    print(tuple([letter_count, int(key)]), end=" ")
