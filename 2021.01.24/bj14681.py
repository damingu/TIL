x = int(input())
y = int(input())
if x > 0 and y > 0 : # 제1사분면
    print(1)
elif x < 0 and y > 0 : # 제2사분면
    print(2)
elif x < 0 and y < 0 : # 제3사분면
    print(3)
else :
    print(4)
