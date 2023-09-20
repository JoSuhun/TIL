import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

heap = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0: continue
        heapq.heappush(heap, (-1*arr[i][j], i, j))
for _ in range(3):
    c, s, e = heapq.heappop(heap)
    print(f'{chr(65+s)}-{chr(65+e)} {-1*c}')