boys = [int(input()) for _ in range(9)]

used = [0]*9
path = [0]*7
lst = []
def choice(start, now, SUM):
    global lst
    if now == 7:
        if SUM == 100:
            lst = path[:]
        return


    for i in range(start, 9):
        if used[i] == 1: continue
        used[i] = 1
        path[now] = boys[i]
        choice(i+1, now+1, SUM + boys[i])
        used[i] = 0

choice(0,0,0)
lst.sort()
for i in lst:
    print(i)