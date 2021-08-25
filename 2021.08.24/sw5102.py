def bfs(s):
    global result
    visited[s] = True
    # 경로
    Q.append(s)
    while Q :
        now_node = Q.pop(0)
        # nowNode와 연결 됐으면서 방문 안한 노드 (BFS)
        for next_node in range(1, V+1):
            if graph[now_node][next_node] and not visited[next_node]:
                Q.append(next_node)
                visited[next_node] = True
                distance[next_node] = distance[now_node] + 1
                # 탈출 조건
                if next_node == e :
                    result = distance[next_node]
                    return
    return

T = int(input())

for tc in range(1, T+1):
    # V : 노드 개수, E : 간선 정보
    V, E = map(int, input().split())
    # 연결 그래프
    graph = [ [0] * (V+1) for _ in range(V+1) ]
    # 방문 기록
    visited = [False] * (V+1)
    # 노드
    Q = []
    # 시작노드에서 idx노드까지의 거리
    distance = [0] * (V+1)
    # 최소 거리
    result = 0

    for i in range(E):
        x,y = map(int, input().split())
        # 무방향성 그래프
        graph[x][y] = 1
        graph[y][x] = 1
    s, e = map(int, input().split())
    bfs(s)
    print(f'#{tc} {result}')