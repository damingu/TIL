n = int(input())
for i in range(1, n+1):
    # 오른쪽 정렬 : rjust(n칸자리수) // 1개인자 필수
    print(('*' * i).rjust(n))