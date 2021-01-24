import sys
n = int(input())
for i in range(n):
    # input()보다 sys.stdin.readline은 대기시간이 없어 속도가 훨씬 빠르다
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)