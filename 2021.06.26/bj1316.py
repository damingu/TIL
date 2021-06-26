n = int(input())
# 그룹단어 갯수
cnt = n
for _ in range(n):
    # 알파벳을 담을 인덱스
    alpha = [0] * 26
    # 단어
    word = input()
    # 단어의 길이만큼
    for j in range(len(word)):
        if j < len(word)-1  :
            if alpha[ord(word[j])-97] == 0 :
                if word[j] != word[j+1] :
                    alpha[ord(word[j])-97] = 1
            else :
                cnt -= 1
                break
        else:
            if alpha[ord(word[len(word)-1])-97] != 0 :
                cnt -= 1
print(cnt)