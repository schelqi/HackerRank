def get_score(word):
    score = 0
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            score += 1
    return 2 if score % 2 == 0 else 1

def score_words(words):
    score = 0
    for word in words:
        score += get_score(word)
    return score


n = int(input())
words = input().split()
# print(words)
print(score_words(words))
