n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

cnt = 0
for coin in coins:
        if k//coin == 0: continue
        cnt += (k//coin)
        k = k % coin
print(cnt)