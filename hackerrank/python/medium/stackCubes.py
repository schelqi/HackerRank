from collections import deque

t = int(input())

for _ in range(t):
    cubes_stacked = True
    n = int(input())
    d = deque()
    d.extend(map(int, input().strip().split()))
    last = 0
    for _ in range(0, n, 2):
        right = d.pop()
        if len(d) > 0:
            left = d.popleft()
            if max(right, left) <= last or last == 0:
                if right >= left:
                    last = right
                    d.appendleft(left)
                else:
                    last = left
                    d.append(right)
            else:
                cubes_stacked = False
                break
        elif right > last:
            cubes_stacked = False

    print("Yes" if cubes_stacked else "No")
