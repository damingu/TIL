# N : 1 ~ N까지 수, M : 수열의 갯수
N, M = map(int, input().split())

stack = []
def dfs():
    # 재귀 탈출 조건
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    # 수열을 만드는 함수
    for i in range(1, N + 1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()
dfs()