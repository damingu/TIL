n = int(input())
temp = list(map(int, input().split()))
minN = 1000000
maxN = -1000000
for i in range(n):
    # 최대값과 최소값을 동시에 구하겠다.
    if minN > temp[i]:
        minN = temp[i]
    if maxN < temp[i] :
        maxN = temp[i]
print(minN, maxN)