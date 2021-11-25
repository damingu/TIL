def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for next in range(n+1):
        if not visited[next] and graph[v][next] == 1 :
            dfs(next)

n, m, v = map(int, input().split())
graph = [ [0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    r, c = map(int, input().split())
    graph[r][c] = 1
    graph[c][r] = 1
dfs(v)
