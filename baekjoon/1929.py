m, n = map(int, input().split())
nn = int(n**0.5)
arr = [0]*(n+1)
for i in range(2, nn+1):
    if arr[i] == 0:
        for j in range(i+i, n+1, i):
            arr[j] = 1
for i in range(m,n+1):
    if i<2: continue
    if arr[i] == 0: print(i)