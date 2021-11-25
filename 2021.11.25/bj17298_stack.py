n = int(input())
A = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    # 옆자리 값이 더 작으면 일단 stack에 쌓아 두고 다음거 검사 -> 큰 값이 나오면 stack에 쌓있는 해결하지 못한 값과 비교
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

for i in range(n):
    print(answer[i], end=" ")