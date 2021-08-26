# N :  1 ~ N까지 자연수, M : 길이가 M인 수열을 모두 구하는 프로그램
N, M = map(int, input().split())

stack = []
def dfs():
    if len(stack) == M :
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(1, N+1):
            stack.append(i)
            dfs()
            stack.pop()

dfs()
