import heapq

n = int(input())
heap = [500]
heapq.heapify(heap)

mid = 500
small = []
large = []
heapq.heapify(small)
heapq.heapify(large)
now = 1
while now <= n:
    a, b = map(int, input().split())

    if a < mid: heapq.heappush(small, -1*a)
    else:heapq.heappush(large, a)
    if b < mid: heapq.heappush(small, -1*b)
    else: heapq.heappush(large, b)

    if len(small)-len(large) == 2:
        heapq.heappush(large, mid)
        mid = -heapq.heappop(small)
    elif len(large)-len(small) == 2:
        heapq.heappush(small, -1*mid)
        mid = heapq.heappop(large)
    print(mid)

    now += 1