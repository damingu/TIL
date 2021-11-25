n = int(input())
m = list(map(int, input().split()))

# 오큰수
def NGE(i):
    # 큰 수 중에 가장 왼쪽에 있는 수
    for j in range(i+1, n):
        if m[i] < m[j] :
            return m[j]
    # 없으면 -1
    return -1
# for반복문 2번으로 O(n^2) 시간 초과
for i in range(n):
    print(NGE(i))
