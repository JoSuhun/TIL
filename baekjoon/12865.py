import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = [[0, 0]]
for _ in range(1, n+1):
    lst.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):     # 가방 개수 만큼 반복
    for j in range(1, k+1): # 최대 무게까지 반복
        w = lst[i][0]
        v = lst[i][1]
        if j < w: dp[i][j] = dp[i-1][j]     # 가방에 넣을 수 없음
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])    # 가방에 넣을 수 있음
print(dp[n][k])