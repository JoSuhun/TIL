n = int(input())
now = list(map(int, input()))
fin = list(map(int, input()))

def change(idx):
    for i in range(idx-1, idx+2):
        if i<0 or i>n-1: continue
        if now[i] == 1:
            now[i] = 0
        else:
            now[i] = 1

cnt = 0

for i in range(1, n):
    change(i)
    cnt += 1
    if now == fin: break

if now != fin: print(-1)
else: print(cnt)
