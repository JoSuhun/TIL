arr = [0, 0]+[1]*1000000
for i in range(2, int(1000000**0.5)+1):
    if arr[i] == 1:
        for j in range(i+i, 1000000, i):
            arr[j] = 0

def isSum(num):
    global SUM
    cnt = 2
    while True:
        if cnt > num:
            break
        if num%cnt == 0:
            SUM += cnt
            SUM += num//cnt
        cnt += 1
    return SUM



T = int(input())
for tc in range(T):
    num = int(input())
    ret = 1
    for i in range(2, num+1):
        SUM = 0
        isSum(i)
        ret += SUM
        print(SUM)
    print(ret)

