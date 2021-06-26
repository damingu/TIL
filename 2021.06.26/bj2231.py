n = int(input())
result = 0
i = 1
while i <= n :
    num = str(i)
    temp = i
    if len(num) != 0 :
        # 각 자리수의 합 만들기
        for j in range(len(num)):
            temp += int(num[j])
    # 분해합 찾기
    if temp == n :
        result = num
        break
    i += 1
print(result)


