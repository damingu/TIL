T = int(input())

for tc in range(1, T+1):
    s = input()
    #
    idx = 0
    while idx < len(s) -1 :
        # 같은 문자열일 경우
        if s[idx] == s[idx+1] :
            s = s[:idx] + s[idx+2:]
            idx = 0
        # 다른 문자일 경우
        else:
            idx += 1
    print(f'#{tc} {len(s)}')