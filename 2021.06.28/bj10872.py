n = int(input())
def factorial(n):
    # 탈출 조건을 걸어주는게 재귀에선 매우 중요
    if n == 0 :
        return 1
    else:
       return n * factorial(n-1)

print(factorial(n))