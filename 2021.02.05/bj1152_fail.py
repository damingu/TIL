# 뭘해도 시간초과ㅠ
import sys
sentence = input().split()
# 전체 단어의 수
total = 0
# 리스트 요소와 같다면 숫자 세기
for i in range(len(sentence)):
    cnt = 0
    for j in range(len(sentence)-i):
        # 한 번 비교했던 단어는 비교하지 않으려면 if조건문 안에 범위가 중요하다
        if sentence[i] == sentence[j+i]:
            cnt += 1
    total += cnt
print(total)