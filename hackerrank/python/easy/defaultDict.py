from collections import defaultdict
if __name__ == '__main__':
    A = defaultdict(list)
    n, m = map(int, input().strip().split(' '))
    for i in range(n):
        A[input()].append(i+1)

    for _ in range(m):
        result = A[input()]
        print(*result if len(result) > 0 else [-1])
