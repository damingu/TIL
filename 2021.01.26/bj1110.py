n = input()
# 변하지 않는 비교값
m = n
cnt = 0
#  10보다 작다면 앞에 0을 붙여 두 자리수로 만들기
if int(n) < 10 :
    n = '0' + n
# 1. 새로운 정수 만들기
while True:
    cnt +=1
    num1 = n[1]
    num2 = int(n[0]) + int(n[1])
    if num2 > 9 :
        num2 = str(num2)[1]
    else :
        num2 = str(num2)
    newN = num1 + num2
    # 정수값 비교하기
    if int(newN) == int(m) :
        break
    # 새로운 정수값으로 갱신
    else :
        n = newN
print(cnt)