from collections import Counter

words = [input().strip() for _ in range(int(input()))]
words_counter = Counter(words)
print(len(words_counter))
print(*words_counter.values())

