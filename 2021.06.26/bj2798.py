# 자료형 일괄 변경해주는 함수 : map
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
# 3장으로 만들 수 있는 m과 가장 가까운 숫자 찾기
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            # max조건
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else :
                maxM = cards[i] + cards[j] + cards[k]
                if result <= maxM :
                    result = maxM
print(result)