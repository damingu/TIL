#N : 1~N까지 값 , M : 길이가 M인 수열
N ,M = map(int, input().split())

stack = []
def dfs():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else:
        for i in range(1, N+1):
            if i not in stack :
                stack.append(i)
                dfs()
                stack.pop()

dfs()
