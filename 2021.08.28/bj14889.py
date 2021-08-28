# 각팀의 능력치를 계산 후 차이를 가르쳐 주는 함수
def calAblity(start):
    global minV
    sumV = 0
    sumW = 0
    link = []
    # 링크 초기화
    for i in range(1, N+1):
        if i not in start :
            link.append(i)
    for i in range(N//2):
        for j in range(i+1, N//2):
            # 스타트의 합
            sumV += s[start[i]-1][start[j]-1] + s[start[j]-1][start[i]-1]
            # 링크의 합
            sumW += s[link[i]-1][link[j]-1] + s[link[j]-1][link[i]-1]
    minV = min(abs(sumV-sumW), minV)
    return


# 팀을 짜는 함수
def teamMaker(start):
    if len(stack) == (N//2): # 절반 뽑으면
        # 능력치 계산
        calAblity(stack)
        return
    else:
        for i in range(start, N+1):
            if i not in stack :
                stack.append(i)
                teamMaker(i+1)
                stack.pop()

# N : 인원수 (항상 짝수)
N = int(input())
#s : 능력치
s = [ list(map(int, input().split())) for _ in range(N) ]

stack = []
minV = 1000000000

teamMaker(1)
print(minV)