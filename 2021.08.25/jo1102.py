# 들어오는 명령어 갯수
N = int(input())
stack = []
for i in range(N):
    order = input()
    # stack push
    if order[0] == 'i':
        # append 하는 값이 몇째자리인지 모르기 때문에
        stack.append(order[2:])
    # stack pop
    elif order[0] == 'o':
        if len(stack) == 0 :
            print("empty")
        else:
            # pop() : python3 내장함수로 값을 뽑아내고 출력하는 함수 그 자체
            print(stack.pop())
    # stack length
    elif order[0] == 'c':
        print(len(stack))
