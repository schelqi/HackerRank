from itertools import combinations

n = int(input())
chars = input().split()
k = int(input())
n_combinations = combinations(range(1, n+1), r=k)
a_indices = [i+1 for i in range(n) if chars[i] == 'a']

score = 0
total_combinations = 0
for tp in n_combinations:
    total_combinations += 1
    for i in a_indices:
        if i in tp:
            score += 1
            break

print(round(score/total_combinations, 3))
