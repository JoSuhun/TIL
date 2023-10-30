import sys
input = sys.stdin.readline
n, s = map(int, input().split())
lst = [0]+list(map(int, input().split()))

st = 0
ed = 1
SUM = lst[st]+lst[ed]
cnt = 2
MIN = 21e8
flag = 0
while st<=ed:
    if SUM < s:
        ed +=1
        if ed>n: break
        cnt += 1
        SUM += lst[ed]
    else:
        flag = 1
        MIN = min(MIN, cnt)
        SUM -= lst[st]
        st += 1
        cnt -=1
if flag: print(MIN)
else: print(0)