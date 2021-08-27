# itertools 라이브러리를 사용하는 경우
from itertools import permutations

# n : 수의 갯수
n = int(input())
# num : 수열
num = list(map(int, input().split()))
# op : 연산자 갯수 정보
op = list(map(int, input().split()))  # + - * /
o = ['+', '-', '*', '/']
oper = []

# 컴퓨터가 연산자를 쉽게 알아 먹을 수 있도록 초기화
for i in range(4):
    for j in range(op[i]):
        oper.append(o[i])

oper = list(set(permutations(oper, len(oper))))  # 중복제거

answer = []
# 중복이 제거된 연산자로
for i in oper:
    m = num[0]
    for j in range(n - 1): # 바로 다음 연산자 계산하기 (마치 재귀처럼)
        if i[j] == '+':
            m += num[j + 1]
        elif i[j] == '-':
            m -= num[j + 1]
        elif i[j] == '*':
            m *= num[j + 1]
        else: # 나눗셈의 경우 음수는 마지막에 결과값을 양수로 바꾼다.
            if m // num[j + 1] < 0:
                m = -(-m // num[j + 1])
            else:
                m = m // num[j + 1]
    answer.append(m)
print(max(answer))
print(min(answer))
