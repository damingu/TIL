T = int(input())

# 미로 탈출 함수
def miroE(x,y):
    global result
    # 제자리 루프 방지
    visited.append((x,y))

    # 인덱스 -> 미로 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # index out of range 방지 -> 범위 안에 있을 때
        if nx >= 0 and ny >= 0 and nx < N and ny < N :
            # 0 : 통로
            if miro[nx][ny] == 0 and (nx, ny) not in visited : # 아래 재귀함수에서 x, y를 다시 안부르기 위해 visitied가 필요
                miroE(nx,ny)
            # 3 : 도착
            elif miro[nx][ny] == 3 :
                result = 1
                return




for tc in range(1, T+1):
    # 깊이 내려가기 위한 탐색 조건 (무방향성)
    visited = []
    result = 0
    # N : 미로의 크기
    N = int(input())
    # miro : 미로
    miro = [ list(map(int, input())) for _ in range(N) ]
    for x in range(N):
        for y in range(N):
            # 출발 : 2
            if miro[x][y] == 2 :
                sr, se = x, y
    miroE(sr, se)
    print(f'#{tc} {result}')
