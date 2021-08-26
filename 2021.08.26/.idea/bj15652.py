# N : 1~N까지 자연수 , M : 길이가 M인 수열
N, M = map(int, input().split())

stack = []
def dfs(start):
    if len(stack) == M:
        print(' '.join(map(int, input())))
        return
    else:
        for i in range(start, N+1):
            if i not in stack:
                stack.append(i)
                dfs(i+1)
                stack.pop()

dfs(1)
