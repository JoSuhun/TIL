n, l = map(int, input().split())    # n 신호등 개수 , l 도로 길이



SUM = 0
delay = 0
start = 0
for i in range(n):
    d, r, g = map(int, input().split())     # d 신호등 위치, r 빨강 지속 시간, g 초록 지속 시간
    d-=1

    for x in range(start, d+1):
        delay += 1
    start = d+1


    r_turn = 1
    g_turn = 0
    while True:
        cnt = r*r_turn + g*g_turn - delay
        if cnt > 0:
            if cnt-r > 0:
                delay += 0
                break
            else:
                delay += cnt
                break

        elif cnt <= 0:
            r_turn += 1
            g_turn += 1

delay += l-start

print(delay)