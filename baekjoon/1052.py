n, k = map(int, input().split())
try:
    ret = n
    while True:
        binary = format(n, 'b')
        if binary.count('1') <= k:
            print(n-ret)
            break
        n += 1
except:
    print(-1)