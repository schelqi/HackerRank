if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        try:
            x, y = map(int, input().strip().split(' '))
            print(x//y)
        except (ValueError, ZeroDivisionError) as error:
            print("Error Code:", error)
