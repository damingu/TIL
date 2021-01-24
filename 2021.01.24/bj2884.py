h, m= map(int,input().split())

if m - 45 < 0: # 가지고 있는 분이 45분보다 작으면 시를 깨야함
    if h == 0:
        h = 24
    h -= 1
    m = m -45 + 60
else : # 가지고 있는 시간이 충분하다면
    m = m - 45
print(h, m)



