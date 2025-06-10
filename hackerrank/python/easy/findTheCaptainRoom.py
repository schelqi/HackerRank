if __name__ == '__main__':
    group_size = int(input())
    rooms = list(map(int, input().strip().split(' ')))
    rooms_set = set()
    rooms_duplicates_set = set()
    for room in rooms:
        if room in rooms_set:
            rooms_duplicates_set.add(room)
        else:
            rooms_set.add(room)
    print(rooms_set.difference(rooms_duplicates_set).pop())
