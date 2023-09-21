import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)
mid = int(input())
print(mid)
small = []
large = []
heapq.heapify(small)
heapq.heapify(large)
for i in range(n-1):
    a = int(input())

    if a < mid: heapq.heappush(small, -1*a)
    else:heapq.heappush(large, a)

    if len(small)-len(large) == 1:
        heapq.heappush(large, mid)
        mid = -heapq.heappop(small)
    elif len(large)-len(small) == 2:
        heapq.heappush(small, -1*mid)
        mid = heapq.heappop(large)

    print(mid)