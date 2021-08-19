T = int(input())
for test_case in range(1, T+1) :
    sentence = input()
    stack = []
    for i in range(len(sentence)):
        if sentence[i] == '(' or sentence[i] == '{' : # 왼쪽괄호이면 stack에 넣어
            stack.append(sentence[i])
        elif sentence[i] == ')' or sentence[i] == '}' : # 오른쪽이면 stack에 있는 괄호 pop 해서 비교
            if len(stack) == 0 : # 처음부터 닫는 괄호가 오는 경우
                stack = [sentence[i]]
                break
            # stack에서 꺼낸 괄호의 종류 2개 중 여는 괄호와 닫는 괄호가 맞지 않는경우
            elif (sentence[i] == ')' and stack[-1] !='(') or (sentence[i] == '}' and stack[-1] != '{'):
                stack = [sentence[i]]
                break
            else : # 괄호의 짝이 맞으면 stack에서 꺼내서 괄호 수 줄여줌
                stack.pop()

    if not len(stack):
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')