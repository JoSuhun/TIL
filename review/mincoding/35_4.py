import heapq
n= int(input())
cost = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 0: continue
        if lst[j] == -1: continue
        heapq.heappush(cost, (lst[j], i, j))
cnt = 0
MAX = -1
while cnt<10:
    cnt += 1
    c, y, x = heapq.heappop(cost)
    if c*2 > MAX:
        MAX = c*2
    heapq.heappush(cost, (c*2, y, x))
print(f'{MAX*2}만원')