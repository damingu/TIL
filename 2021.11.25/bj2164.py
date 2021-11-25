n = int(input())
m = [ i+1 for i in range(n)]
while len(m) > 1 :
    # 첫번째 카드 버려
    m.pop(0)
    # 제일 위를 맨 아래로 보내
    m.append(m.pop(0))
print(m[0])