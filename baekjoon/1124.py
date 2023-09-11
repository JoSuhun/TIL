def find(num):
    ret = 0
    a = 2
    while a <= num:
        if num % a == 0:
            ret += 1
            num = num//a
        else:
            a += 1
    return ret

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    x = find(i)
    xx = find(x)
    print(xx)
    if xx == 1:
        cnt += 1
print(cnt)
