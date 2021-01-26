while True:
    # 값이 들어오면 계속 받되
    try : 
        a, b = map(int, input().split())
        print(a+b)
    # 값이 안들어오면 반복문을 탈출해라
    except:
        break