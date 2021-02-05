word = input()
alpa = [ 0 for _ in range(26) ]
# 가장 많이 사용되는 알파벳을 출력
for i in range(len(word)):
    # 대, 소문자 구별 X -> 아스키코드로 구별 (A == 65, a == 97)
    # 소문자인 경우
    if ord(word[i]) >= 97 :
        alpa[ord(word[i]) - 97] += 1
    # 대문자인 경우
    elif ord(word[i]) >=65 :
        alpa[ord(word[i]) - 65] += 1
# 가장 많이 사용되는 알파벳 찾기
maxN = max(alpa)
cnt = 0
idx = 9999
many = False
for i in range(26):
    if alpa[i] == maxN :
        cnt += 1
        idx = i
    # 가장많이 사용된 알파벳이 여러개일 경우
    if cnt >= 2 :
        many = True
        break
# 가장 많이 사용된 알파벳 대문자 출력
if many == True :
    print('?')
else :
    print(chr(65+idx))