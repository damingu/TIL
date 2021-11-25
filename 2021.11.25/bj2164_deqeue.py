#시간 초과 방지를 위한 deque
import collections
n = int(input())
m = collections.deque([i for i in range(1, n+1)])

while len(m) > 1 :
    m.popleft() # 왼쪽 요소 제거
    m.rotate(-1) # 왼쪽으로 한바퀴 돌려라

print(m[0])
