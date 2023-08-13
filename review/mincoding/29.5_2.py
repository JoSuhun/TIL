evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]

n = int(input())

def check(now):
    if now == 0: return
    check(evid[now])
    print(f'{now}번index({timeStamp[now]}시)')

print('0번index(출발)')
check(n)