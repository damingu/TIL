# N : 1~N까지 자연수 , M : 길이가 MSSS인 수열
N, M = map(int, input().split())

stack = []
def dfs(start):
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start, N+1):
            stack.append(i)
            dfs(i)
            stack.pop()

dfs(1)
