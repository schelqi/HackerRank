from collections import deque
if __name__ == '__main__':
    N = int(input())
    d = deque()
    for _ in range(N):
        query, *params = input().strip().split(' ')
        if query == "append":
            d.append(*params)
        elif query == "appendleft":
            d.appendleft(*params)
        elif query == "pop":
            d.pop()
        elif query == "popleft":
            d.popleft()
    print(*d)
