T = int(input())

# 게임을 진행하는 함수
def playgame(l_idx, r_idx):
    # 사람 번호 - 인덱스 = 1
    l,r = cards[l_idx-1], cards[r_idx-1]
    if l == r :
        return l_idx
    elif l == 1 : # 1 : 가위
        if r == 3 : return l_idx # 3 : 보
        elif r == 2: return r_idx # 2 : 바위
    elif l == 2 : # 2 : 바위
        if r == 1: return l_idx # 1 : 가위
        elif r == 3 : return r_idx # 3 : 보
    elif l == 3 : # 3 : 보
        if r == 2 : return l_idx # 2 : 바위
        elif r == 1 : return r_idx # 1 : 가위

#토너먼트 경기 대진표
def gameSchedule(s, e):
    if s == e :
        return s
    else:
        mid = (s+e) // 2
        l = gameSchedule(s, mid)
        r = gameSchedule(mid+1, e)
        return playgame(l, r)

for tc in range(1, T+1):
    # N : 인원수
    N = int(input())
    # cards : 참여자들 카드 정보
    cards = list(map(int, input().split()))
    # 카드게임 우승자
    winner = gameSchedule(1,N)
    print(f'#{tc} {winner}')
