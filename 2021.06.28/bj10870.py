n = int(input())
def fibonacci(n):
    # 피보나치의 경우 0번쨰는 0
    if n == 0 :
        return 0
    # 1번째는 1로 탈출 조건 1
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))
