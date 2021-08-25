N = input()

# 처음은 방향 관계 없이 무조건 높이 10cm
result = 10
for i in range(0, len(N)-1):
    # 같은 방향의 접시라면 높이 5
    if N[i] == N[i+1]:
        result += 5
    # 다른 방향이라면 높이 10
    elif N[i] != N[i+1]:
        result += 10
print(result)
