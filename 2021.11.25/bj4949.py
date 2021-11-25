while True:
    s = input()
    stack = list()
    # 괄호가 하나도 없는 경우도 균형잡힌 문자열
    if s == '.':
        break
    for i in range(len(s)):
        # 왼쪽 괄호이면 stack에 넣기
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])
        # 소괄호 짝맞추기
        elif s[i] == ')':
            # 0이 아닐때 pop 가능
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])
                break
        # 대괄호 짝맞추기
        elif s[i] == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[i])
                break

    # 정답 추출(소문자 출력)
    if len(stack) == 0 :
        print("yes")
    else:
        print("no")
