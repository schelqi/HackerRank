from itertools import product

if __name__ == '__main__':
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    result = product(A, B)
    print(*list(result))