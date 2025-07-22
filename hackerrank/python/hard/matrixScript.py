import re
chars_to_replace = r"[a-zA-Z0-9]([!@#$%&\s]+)[a-zA-Z0-9]"

n, m = map(int, input().split())
matrix = list()
for _ in range(n):
    matrix.append(list(input()))

zipped_matrix = zip(*matrix)

words = [''.join(x) for x in zipped_matrix]
sentence = ''.join(words)

for x in re.findall(chars_to_replace, sentence):
    sentence = sentence.replace(x, ' ', 1)

print(sentence)
