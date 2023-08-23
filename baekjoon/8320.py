n = int(input())
now = 1
cnt = 0
while now <= n:
    for i in range(now, n+1):
        if now * i <= n:
            cnt += 1
    now += 1
print(cnt)