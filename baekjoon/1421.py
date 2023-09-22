n, c, w = map(int, input().split())
woods = [int(input()) for _ in range(n)]

MAX = 0
for cm in range(1, max(woods)+1):
    cnt = 0
    total = 0
    cut = 0
    for wood in woods:
        if cm > wood: continue
        cnt = wood//cm
        if wood % cm == 0:
            cut = cnt -1
        else:
            cut = cnt
        ret = cnt*cm*w - cut*c
        if ret >= 0:
            total += ret

    MAX = max(total, MAX)

print(MAX)
