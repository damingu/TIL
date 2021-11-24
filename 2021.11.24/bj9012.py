n = int(input())
for _ in range(n):
    i = input()
    # stack에 첫 요소 담아 놓고 시작
    stack = [i[0]]
    for j in range(1, len(i)):
        # stack에 요소가 있을 때 pop 가능
        if len(stack) != 0 :
            # 괄호가 다른경우
            if stack[-1] != i[j] :
                # VPS가 아닌경우 예외처리
                if stack[-1] == ')' and i[j] == '(':
                    stack.append(i[j])
                else :
                    stack.pop()
            # 괄호가 같은 경우
            else:
                stack.append(i[j])
        # 중간에 stack이 비는 경우
        else:
            stack.append(i[j])

    if len(stack) != 0:
        print("NO")
    else :
        print("YES")