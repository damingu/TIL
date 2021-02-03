# 등차수열인지 검사하는 함수
def isHan(n):
    # 1의 자리, 10의 자리에선 무조건 한수
    if n < 99 :
        return True
    # 100의 자리에서 부터 검사 필요
    else:
        temp = str(n)
        # 사실 조건이 1000보다 작은수이기 떄문에 많아야 세자리수.. 코드가 훨씬 간결해 질 수 있음
        for i in range(len(temp)-2):
            if int(temp[i]) - int(temp[i+1]) != int(temp[i+1]) -int(temp[i+2]) :
                return False
        return True

n = int(input())
total = 0
for i in range(1,n+1) :
    han = False
    han = isHan(i)
    if han == True :
        total += 1
print(total)
