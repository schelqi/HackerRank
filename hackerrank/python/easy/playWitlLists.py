

if __name__ == '__main__':
    N = int(input())
    data = list()
    for _ in range(N):
        query, *params = input().strip().split(' ')

        if query == "insert":
            position, value = map(int, params)
            data.insert(position, value)
        elif query == "print":
            print(data)
        elif query == "remove":
            data.remove(int(params[0]))
        elif query == "append":
            data.append(int(params[0]))
        elif query == "sort":
            data.sort()
        elif query == "pop":
            data.pop()
        elif query == "reverse":
            data.reverse()

