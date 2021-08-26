# N : 1~N 자연수, M : 길이가 M인 수열
N, M = map(int, input().split())

stack = []

# 중복 없이 M, 오름차순
def dfs(start):
    # 탈출 조건
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(start, N+1):
            if i not in stack:
                stack.append(i)
                dfs(i+1)
                stack.pop()

dfs(1)