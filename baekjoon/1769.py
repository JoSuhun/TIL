n = list(map(int, input()))

cnt = 0
while True:
    ret = sum(n)
    if len(n) == 1 and ret < 10:
        break

    n = list(map(int, str(ret)))
    cnt += 1

print(cnt)
if ret % 3 == 0:
    print('YES')
else:
    print('NO')