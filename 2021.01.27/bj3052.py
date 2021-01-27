num = list()
cnt = 0
for _ in range(10) :
    n = int(input()) % 42
    # 없으면 넣고
    if n not in num :
        num.append(n)
        cnt += 1
    # 있으면 넣지마
    else :
        continue
print(cnt)