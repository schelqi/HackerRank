if __name__ == '__main__':
    A = set(map(int, input().strip().split(' ')))
    result = list()
    test_cases = int(input())
    for _ in range(test_cases):
        B = set(map(int, input().strip().split(' ')))
        result.append(A.issuperset(B))

    print(all(result))


