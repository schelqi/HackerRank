cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return list()
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(n - 2):
        result.append(sum(result[i:i+2]))
    return result


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
