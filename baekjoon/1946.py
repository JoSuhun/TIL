import heapq
T = int(input())
for tc in range(T):
    n = int(input())
    scores = []
    for _ in range(n):
        v1, v2 = map(int,input().split())
        scores.append((v1, v2))
    scores.sort()
    cnt = 1
    v2 = scores[0][1]
    for i in range(1, n):
        if v2 > scores[i][1]:
            cnt += 1
            v2 = scores[i][1]
    print(cnt)