st1 = list(input())
st2 = list(input())

n = len(st1)
m = len(st2)


lst =[]
def sameStr(x,y):
    global lst
    if x>=n or y>=m:
        return lst
    if st1[x] == st2[y]:
        lst.append(st1[x])
        sameStr(x+1,y+1)
    return lst

result = []
for i in range(n):
    for j in range(m):
        if st1[i] == st2[j]:
            ret = sameStr(i,j)
            result.append(ret)
            lst = []

MAX = -1
for i in result:
    if len(i) > MAX:
        MAX = len(i)
        MAX_str = i
print(*MAX_str, sep='')