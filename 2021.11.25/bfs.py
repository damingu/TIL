def bfs(v):
    Q.append(v)
    visited[v] = True
    while Q :
        # 맨 앞에서 부터
        s = Q.pop(0)
        print(s, end=' ')
        for next in range(1,n+1):
            if graph[s][next] and not visited[next] :
                # 해당 노드와 연결된 노드들을 다 기록
                Q.append(next)
                visited[next] = True


n, m, v = map(int, input().split())
graph = [ [0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
Q = []

for _ in range(m):
    r, c = map(int, input().split())
    graph[r][c] = 1
    graph[c][r] = 1

bfs(v)