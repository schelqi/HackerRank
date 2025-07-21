for i in range(1, int(input())):
    print(i + i*sum(map(lambda j: 10**j, range(1, i))))
