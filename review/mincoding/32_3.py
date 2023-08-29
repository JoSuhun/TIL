n = int(input())
bombs = list(map(int, input().split()))

for i in range(1, n-1):
    if bombs[i-1] == bombs[i] and bombs[i] == bombs[i+1]:
        bombs[i-1] = 0
        bombs[i] = 0
        bombs[i+1] = 0
bombs.sort()
for bomb in bombs:
    if bomb == 0: continue
    print(bomb,end=' ')