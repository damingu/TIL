N = [ list(input()) for _ in range(5)]

# 한개의 열에 최대 15줄
pan = [ ['-1'] * 15 for _ in range(5)]

for i in range(5):
    for j in range(len(N[i])):
        pan[i][j] = N[i][j]

# 값 출력
for c in range(15):
    for r in range(5):
        if pan[r][c] == '-1':
            continue
        print(pan[r][c], end='')