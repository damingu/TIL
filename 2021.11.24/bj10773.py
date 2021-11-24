n = int(input())
stack = []
for _ in range(n):
    i = int(input())
    if i == 0 :
        if len(stack) != 0 :
            stack.pop()
    else :
        stack.append(i)
# 재민이가 최종적으로 적어 낸 수의 합
print(sum(stack))