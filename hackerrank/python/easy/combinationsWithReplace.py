from itertools import combinations_with_replacement

if __name__ == '__main__':
    word, n = input().split(' ')
    result = [''.join(sub_word) for sub_word in combinations_with_replacement(sorted(word), int(n))]
    print(*result, sep="\n")
