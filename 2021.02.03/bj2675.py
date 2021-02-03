t = int(input())
for i in range(t):
    newS = ''
    r, word = input().split()
    # 각 알파벳을
    for k in range(len(word)):
        # r번씩 반복해라.
        for j in range(int(r)):
            newS += word[k]
    print(newS)