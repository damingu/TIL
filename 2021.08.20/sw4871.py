T = int(input())

# 깊이 우선으로 경로를 찾는 함수
def DFS(s):
    global result
    visited[s] = 1
    for next in range(0, V):
        if g[s][next] and visited[next] == 0 :
            if next == e : # 재귀 탈출 조건
                result = 1
                return
            DFS(next)

for tc in range(1, T+1):
    result = 0
    # V : 노드, E : 간선
    V, E = map(int, input().split())
    # 그래프를 담을 자료 구조
    g = [ [0] * V for _ in range(V) ]
    # 방문했는지 확인하는 자료구조
    visited = [False] * V
    # 1. 방향성 그래프 그리기
    for _ in range(0, E):
        x, y = map(int, input().split())
        # 방향성 그래프
        g[x-1][y-1] = 1
    # s : 출발 노드, e : 도착노드
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    DFS(s)
    print(f'#{tc} {result}')