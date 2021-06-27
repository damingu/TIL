N = 9
mine = [ [1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6] ]

def solution(N, mine):
    answer = []
    tempMap = makeMine(N, mine)
    print(tempMap)
    # 전체판을 돌면서 지뢰가 있는지 확인
    for i in range(N):
        for j in range(N):
            if tempMap[i][j] != -1 :
                answer = getCnt(i, j, tempMap, N)
    print(answer)
    return answer

# 지뢰를 배치하는 함수
def makeMine(N, mine) :
    pan = [[0] * N for _ in range(N)]
    # 지뢰를 먼저 배치
    for i in range(len(mine)):
        a, b = mine[i]
        pan[a-1][b-1] = -1
    return pan

# 지뢰를 세는 함수
def getCnt(x, y, tempMap, N):
    cnt = 0
    dx = [ -1, 0, 1]
    dy = [-1, 0, 1]
    for i in range(3):
        for j in range(3):
            newX = x + dx[i]
            newY = y + dy[j]
            #인덱스가 범위를 넘어서면 안돼
            if newX >= 0 and newX < N and newY >= 0 and newY < N :
                if tempMap[newX][newY] == -1 :
                    cnt += 1
    # 지뢰를 다 셌으면 해당 값 갱신
    tempMap[x][y] = cnt
    return tempMap

solution(N, mine)