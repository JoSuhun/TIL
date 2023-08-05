# N, M = map(int, input().split())

# arrs = []
# for _ in range(N):
#     arrs.append(list(map(int, input().split())))

# arr_SUM_lst = []

# for arr in arrs:
#     SUM_lst = [0]
#     SUM = 0
#     for a in arr:
#         SUM += a
#         SUM_lst.append(SUM)
#     arr_SUM_lst.append(SUM_lst)

# for tc in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     for x in range(x1-1, x2):
#         total += arr_SUM_lst[x][y2] - arr_SUM_lst[x][y1-1]
#     print(total)

# # 런 타임 오류


# # 구간합으로 풀어보자!
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arrs = [[0]*(n+1)]

for _ in range(n):
    arr = [0] + list(map(int, input().split()))
    arrs.append(arr)

d_arrs = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        d_arrs[i][j] = d_arrs[i][j-1] + \
            d_arrs[i-1][j] - d_arrs[i-1][j-1] + arrs[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = d_arrs[x2][y2] - d_arrs[x1-1][y2] - \
        d_arrs[x2][y1-1] + d_arrs[x1-1][y1-1]

    print(result)
