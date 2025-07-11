from collections import Counter

word = input().strip()
word_counter = Counter(word)

sorted_word_counter = sorted(word_counter.items(), key=lambda item: (-item[1], item[0]))
for i in range(3):
    print(*sorted_word_counter[i])
