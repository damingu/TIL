T = int(input())

# minV를 구하는 함수
def calc(row):
    global minV, sumV
    # 가지치기
    if minV > sumV :
        return
    # 재귀 탈출 조건
    if row == N :
        if minV < sumV:
            sumV = minV
        return
    #부분집합 만드는 코드
    for i in range(N):
        if not visited[i]: # x가 false라면
            visited[i] = True # 방문
            minV += pan[row][i] #minV 갱신
            calc(row+1)
            visited[i] = False
            minV -= pan[row][i]

for tc in range(1, T+1):
    N = int(input())
    pan = [ list(map(int, input().split())) for _ in range(N)]
    visited =[0] * N
    # DP를 위한 minV, sumV
    minV, sumV = 0, 999999999

    calc(0)



