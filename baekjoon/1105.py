l, r = map(int, input().split())
cnt = 0
k = list(str(r-l))
print(k)
for i in range(len(k)):
    print(str(r)[i])
    print(k[i])
    if k[i] == '0' and str(r)[i] == '8':
        cnt += 1
print(cnt)