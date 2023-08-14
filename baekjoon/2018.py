n = int(input())

cnt = 1
start = 1
end = 1
SUM = 1

while end != n:
    if SUM < n:
        end += 1
        SUM += end
    elif SUM == n:
        cnt += 1
        SUM -= start
        start +=1
    elif SUM > n:
        start += 1
        SUM -= start

print(cnt)