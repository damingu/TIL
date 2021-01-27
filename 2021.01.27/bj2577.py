A, B, C = [ int(input()) for _ in range(3)]
num = A * B * C
# 숫자가 몇개 있는지 세어주는 list
cnt = [ 0 for _ in range(10)]
# num 의 길이
num = str(num)
lgt = len(num)
for i in range(lgt) :
    cnt[int(num[i])] += 1
# 다시 출력
for i in range(10) :
    print(cnt[i])