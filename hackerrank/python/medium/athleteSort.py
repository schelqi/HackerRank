
if __name__ == '__main__':
    n, m = map(int, input().split())
    data = list()
    for _ in range(n):
        data.append(list(map(int, input().split())))
    k = int(input())
    sorted_data = sorted(data, key=lambda x: x[k])
    for row in sorted_data:
        print(*row)