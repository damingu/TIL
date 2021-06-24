# 상수 2개를 입력 받음
a, b = input().split()
# 상수가 보는 숫자, input type == str
a = int(a[::-1])
b = int(b[::-1])
# 값 비교
if a > b :
    print(a)
else:
    print(b)