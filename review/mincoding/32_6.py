n, c = map(int, input().split())
lst = [list(map(str, input().split())) for _ in range(c)]
ans = sorted(lst, key=lambda x: int(x[0]))

bucket = [0]*n
for a in ans:
    bucket[int(a[0])] += 1

idx = bucket.index(max(bucket))
for b in bucket:
    if b == idx:
        idx = b
        break
for a in ans:
    if int(a[0]) == idx:
        print(a[1], end=' ')