n = int(input())    # 기둥 개수
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: x[0])

max_h = -1
max_idx = 0

for i in range(n):
    if lst[i][1] > max_h:
        max_h = lst[i][1]
        max_idx = i



SUM = 0
now_h = lst[0][1]
for i in range(max_idx):
    if lst[i][1] < lst[i+1][1]:
        SUM += (lst[i + 1][0] - lst[i][0]) * now_h
        now_h = max(lst[i+1][1], now_h)
    else:
        SUM += (lst[i + 1][0] - lst[i][0]) * now_h

now_h = lst[-1][1]
for i in range(n-1, max_idx, -1):
    if lst[i][1] < lst[i-1][1]:
        SUM += (lst[i][0] - lst[i - 1][0]) * now_h
        now_h = max(lst[i-1][1], now_h)
    else:
        SUM += (lst[i][0] - lst[i-1][0]) * now_h


print(SUM+max_h)