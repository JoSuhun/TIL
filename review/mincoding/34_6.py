import heapq
n = int(input())
poket = list(map(int, input().split()))
heapq.heapify(poket)
backup = poket[:]

cnt = 0
while poket:
    x = heapq.heappop(poket)
    if x not in backup: break
    heapq.heappop(backup)
    cnt += 1
    y = heapq.heappop(poket)
    if y not in backup: break
    heapq.heappop(backup)
    cnt += 1
    heapq.heappush(poket, 2*y)
print(cnt)