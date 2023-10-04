n = int(input())
primary = [0, 0] + [1]*10000001
for i in range(2, int(len(primary)**0.5)+1):
    if primary[i] == 1:
        for j in range(i+i, len(primary), i):
            primary[j] = 0

def ispalin(num):
    numlst = list(str(num))
    st = 0
    ed = len(numlst)-1
    flag = 1
    while st<ed:
        if numlst[st] == numlst[ed]:
            st += 1
            ed -= 1
        else:
            flag = 0
            break
    if flag: return 1
    else: return 0

for i in range(n, len(primary)):
    if primary[i]:
        if ispalin(i):
            print(i)
            break
