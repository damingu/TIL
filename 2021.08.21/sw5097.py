T = int(input())

for tc in range(1, T+1):
    # N : 수열의 갯수, M : 맨뒤로 보내는 작업
    N, M = map(int, input().split())
    order = list(map(int, input().split()))
    # 원형 큐로 해결
    ans = order[(M % N)]
    print(f'#{tc} {ans}')