sentence = input().strip()
if(len(sentence)) == 0 :
    print(0)
else:
    # 한 단어가 여러번 등장해도 횟수만큼 세어야 한다 -> 문장안의 띄어쓰기로 숫자 세도 괜츈
    print(sentence.count(' ')+1)