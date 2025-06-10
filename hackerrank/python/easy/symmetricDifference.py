if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().strip().split(' ')))
    m = int(input())
    set2 = set(map(int, input().strip().split(' ')))
    result = list(set1.symmetric_difference(set2))
    result.sort()
    print(*result, sep="\n")
