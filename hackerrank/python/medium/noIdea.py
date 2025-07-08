
n, m = map(int, input().split())
X = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness_score = 0
for i in X:
    if i in A:
        happiness_score += 1
    elif i in B:
        happiness_score -= 1

print(happiness_score)