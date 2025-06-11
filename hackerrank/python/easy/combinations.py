from itertools import combinations
if __name__ == '__main__':
    word, n = input().split(' ')

    for i in range(1, int(n) + 1):
        result = [''.join(sub_word) for sub_word in combinations(sorted(word), i)]
        # result.sort()
        print(*result, sep="\n")
