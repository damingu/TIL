n = int(input())
score = list(map(int, input().split()))
maxN = max(score)
total = 0
for i in range(n):
    total += score[i] / maxN * 100
print(total / n )