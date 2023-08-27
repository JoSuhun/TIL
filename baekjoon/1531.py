n, m = map(int, input().split())    # n개의 가리는 종이 // m 개 이상일 때 가려짐
cnt = 0
arrs = [[0]*100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            arrs[i][j] += 1
for i in range(100):
    for j in range(100):
        if arrs[i][j] > m:
            cnt += 1
print(cnt)