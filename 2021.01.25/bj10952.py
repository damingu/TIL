start = True
while start :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        start = False
        # while문을 바로 탈출해 이 밑으로는 실행을 할 수 없도록 해야함
        break
    print(A + B)

