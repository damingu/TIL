T = int(input())
for _ in range(T):
    temp = input()
    cnt = 0
    ans = 0
    for i in range(len(temp)):
        # 연속 O 수 세다가 X 나오면 다시 세기
        if temp[i] == 'O' :
            cnt += 1
        elif temp[i] == 'X':
            cnt = 0
        ans += cnt
    print(ans)