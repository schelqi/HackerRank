from itertools import product

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    data = product(range(x + 1), range(y + 1), range(z + 1))

    result = [[i, j, k] for (i, j, k) in data if i + j + k != n]
    print(result)
