if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split(' ')))
    m = int(input())
    for _ in range(m):
        query, *params = input().split(' ')
        try:
            if query == "pop":
                A.pop()
            elif query in ("remove", "discard"):
                A.remove(int(params[0]))
        except KeyError as error:
            pass
    print(sum(A))


