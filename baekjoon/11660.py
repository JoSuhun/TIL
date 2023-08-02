N, M = map(int, input().split())

arrs = []
for _ in range(N):
    arrs.append(list(map(int, input().split())))

arr_SUM_lst = []

for arr in arrs:
    SUM_lst = [0]
    SUM = 0
    for a in arr:
        SUM += a
        SUM_lst.append(SUM)
    arr_SUM_lst.append(SUM_lst)

for tc in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for x in range(x1-1, x2):
        total += arr_SUM_lst[x][y2] - arr_SUM_lst[x][y1-1]
    print(total)

# 우욱..
