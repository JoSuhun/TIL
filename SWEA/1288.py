T = int(input())


def isTrue(lst):
    flag = 1
    for i in lst:
        if i == 0:
            flag = 0
            break
    return flag


for tc in range(1, T+1):
    n = int(input())

    bucket = [0]*10
    x = 0

    while True:
        x += 1
        for i in list(str(n*x)):
            bucket[int(i)] += 1

        if isTrue(bucket): break

    print(f'#{tc} {n*x}')

