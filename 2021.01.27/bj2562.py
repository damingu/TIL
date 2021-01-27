# Enter로 구분된 값들을 받아서 list로 만들어줌
num = [ int(input()) for _ in range(9)]
maxN = 0
max_idx = 0
for i in range(9):
    if maxN < num[i] :
        maxN = num[i]
        # 번째 == 인덱스 + 1
        max_idx = i+1
print(maxN)
print(max_idx)