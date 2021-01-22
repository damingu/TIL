A = int(input())
B = int(input())
midleB = str(B)
for i in range(len(midleB)-1,-1,-1):
    print(A * int(midleB[i]))
print(A*B)