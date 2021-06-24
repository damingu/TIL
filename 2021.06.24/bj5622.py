dial = input()
total = len(dial)
for i in range(len(dial)) :
    # 문자에 맞는 숫자 조건문
    if dial[i] == 'A' or dial[i] == 'B' or dial[i] == 'C':
        total += 2
    elif dial[i] == 'D' or dial[i] == 'E' or dial[i] == 'F':
        total += 3
    elif dial[i] == 'G' or dial[i] == 'H' or dial[i] == 'I':
        total += 4
    elif dial[i] == 'J' or dial[i] == 'K' or dial[i] == 'L':
        total += 5
    elif dial[i] == 'M' or dial[i] == 'N' or dial[i] == 'O':
        total += 6
    elif dial[i] == 'P' or dial[i] == 'Q' or dial[i] == 'R' or dial[i] == 'S':
        total += 7
    elif dial[i] == 'T' or dial[i] == 'U' or dial[i] == 'V':
        total += 8
    elif dial[i] == 'W' or dial[i] == 'X' or dial[i] == 'Y' or dial[i] == 'Z':
        total += 9
    else:
        total += 0
print(total)