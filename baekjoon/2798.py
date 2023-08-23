n, m = map(int, input().split())    # n 카드 개수, m 설정 값
card = list(map(int, input().split()))

used = [0]*n
path = [0]*3
lst = []
def choice(now):
    global lst

    if now == 3:
        SUM = 0
        for i in range(3):
            SUM += path[i]
        lst.append(SUM)
        return

    for i in range(n):
        if used[i] == 1: continue
        path[now] = card[i]
        used[i] = 1
        choice(now+1)
        used[i] = 0
choice(0)

MIN = 21e8

for l in lst:
    if m-l < MIN and m-l >= 0:
        MIN = m-l
        ret = l
print(ret)