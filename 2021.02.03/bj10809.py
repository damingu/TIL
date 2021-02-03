word = input()
alpa = [ -1 for _ in range(26) ]
# 단어에 스펠링이 들어있는지 확인
for i in range(len(word)) :
    # 알파벳이 처음 등장하는 위치 값을 넣어야 함
    if alpa[(ord(word[i]))-97] == -1 :
        # 문자 -> 숫자 (소문자 a의 아스키코드값 == 97)
        alpa[(ord(word[i]))-97] = i
    else:
        continue
for i in alpa:
    print('{}' .format(i), end=" ")