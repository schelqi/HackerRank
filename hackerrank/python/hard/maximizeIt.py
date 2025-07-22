from itertools import product

k, M = map(int, input().split())
data = list()
max_sum = 0
for _ in range(k):
    data.append(list(map(lambda i: (int(i) ** 2) % M, input().split()[1::])))


for x in product(*data):
    x_sum = sum(x) % M
    if x_sum > max_sum:
        max_sum = x_sum

print(max_sum)
