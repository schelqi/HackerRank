if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int, input().strip().split(' ')))
    m = int(input())
    for _ in range(m):
        query, k = input().strip().split(' ')
        set2 = set(map(int, input().strip().split(' ')))
        if query == "intersection_update":
            set1.intersection_update(set2)
        elif query == "symmetric_difference_update":
            set1.symmetric_difference_update(set2)
        elif query == "difference_update":
            set1.difference_update(set2)
        elif query == "update":
            set1.update(set2)

    print(sum(set1))