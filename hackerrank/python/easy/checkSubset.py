if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        A = set(map(int, input().strip().split(' ')))
        m = int(input())
        B = set(map(int, input().strip().split(' ')))
        print(A.issubset(B))
