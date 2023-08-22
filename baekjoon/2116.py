import copy
num = int(input())  # num 주사위 개수
arrs = [list(map(int, input().split())) for _ in range(num)]
backup = copy.deepcopy(arrs)

dic = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2}

def choice(idx):
    i = idx
    now = 0
    while now < len(arrs)-1:
        arrs[now][i] = 0
        k = arrs[now][dic[i]]
        arrs[now][dic[i]] = 0
        now += 1
        i = arrs[now].index(k)
    arrs[now][i] = 0
    arrs[now][dic[i]] = 0
    return arrs

MAX = -21e8
for i in range(6):
    choice(i)
    SUM = 0
    for arr in arrs:
        SUM += max(arr)
    if SUM > MAX:
        MAX = SUM
    arrs = copy.deepcopy(backup)

print(MAX)