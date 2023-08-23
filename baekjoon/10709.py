h, w = map(int, input().split())
sky = [list(input()) for _ in range(h)]

result =[[-1]*w for _ in range(h)]

for i in range(h):
    cnt = -1
    for j in range(w):
        if sky[i][j] == 'c':
            result[i][j] = 0

    now = 0
    flag = 0
    while now < w:

        if sky[i][now] == 'c':
            cnt = 0
            flag = 1
        elif flag == 1 and sky[i][now] == '.':
            cnt += 1
            result[i][now] = cnt

        now += 1

for r in result:
    print(*r)
