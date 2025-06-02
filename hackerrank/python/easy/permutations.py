from itertools import permutations

if __name__ == '__main__':
    word, length = input().strip().split(' ')

    data = permutations(word, r=int(length))
    result = [''.join(x) for x in data]
    result.sort()
    print(*result, sep="\n")
