T = int(input())
for i in range(T):
    scr = list(map(int, input().split()))
    cnt = 0
    # 반평균 구하기
    avg = sum(scr[1:]) / scr[0]
    # 평균이 넘는 학생들의 비율을 보여줘야함
    for j in range(scr[0]):
        # 반평균 보다 점수 높은 학생은 cnt 세기
        if scr[j+1] > avg :
            cnt += 1
    #학생들 비율 구하기
    # 소수점 0도 출력할 수 있도록 조정
    print('{0: .3f}%' .format(cnt/scr[0] * 100))
