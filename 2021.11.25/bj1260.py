# 한놈만 판다
def dfs(v):
    visitedDFS[v] = True
    print(v, end=' ')
    for next in range(1, n+1):
        if not visitedDFS[next] and graph[v][next] == 1 :
            dfs(next) # 사실은 stack 구조

# 짧은놈만 판다
def bfs(v):
    Q.append(v)
    visitedBFS[v] = True
    while Q :
        s = Q.pop(0)
        print(s, end=' ')
        for next in range(1, n+1):
            if graph[s][next] and not visitedBFS[next] :
                Q.append(next)
                visitedBFS[next] = True

n, m, v = map(int, input().split())
graph = [ [0] * (n+1) for _ in range(n+1)]
# for dfs
visitedDFS = [False] * (n+1)
# for bfs
visitedBFS = [False] * (n+1)
Q = []

for _ in range(m):
    r, c = map(int, input().split())
    graph[r][c] = 1
    graph[c][r] = 1

dfs(v)
print()
bfs(v)