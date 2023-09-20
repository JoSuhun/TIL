import heapq
lst = input()
heap = []
for i in range(len(lst)):
    heapq.heappush(heap, -1*ord(lst[i]))

while heap:
    ret = -1*heapq.heappop(heap)
    print(chr(ret), end='')