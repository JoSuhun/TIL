## gready
# 파티룸 예약 ..
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# # 끝나는 시간 기준 정렬
# arr.sort(key=lambda x:(x[1], x[0]))
#
# end = 0
# ans = 0
# for i in range(n):
#     if end <= arr[i][0]:
#         end = arr[i][1]
#         ans += 1
# print(ans)

# ----------------------------------------------------------------

## DP dynamic programming


# lst = list(map(int, input().split()))
# lst = [0, 7, -3, -5, -4, -2, 6, 5, -9, -1, 0]
# dp = [0]*len(lst)
# for i in range(1, len(lst)):
#     jp1 = dp[i-1]
#     jp2 = dp[i-2]
#     jp3 = dp[i//2]
#     dp[i] = jp1 + lst[i]
#     if dp[i] < jp2 + lst[i]:
#         dp[i] = jp2 + lst[i]
#     if i%2 == 0 and dp[i] < jp3 + lst[i]:
#         dp[i] = jp3 + lst[i]
# print(dp[10])




# 0,0 에서 3,3 까지 최단거리로 이동한다고 했을때
# 3,3에 도착했을 당시 최소 유류비는 얼마 나올까요??
arr=[
    [0,1,2,2],
    [1,3,4,1],
    [5,8,1,4],
    [9,1,78,0]]

dp = [[0]*4 for _ in range(4)]

SUM1 = 0
SUM2 = 0
for i in range(4):
    SUM1 += arr[0][i]
    dp[0][i] = SUM1
    SUM2 += arr[i][0]
    dp[i][0] = SUM2

for i in range(1, 4):
    for j in range(1, 4):
        dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])
print(dp[3][3])