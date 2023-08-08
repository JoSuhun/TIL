br, lev = map(int, input().split())

cnt = 0
def abc(level):
    global cnt
    cnt +=1
    if level == lev:
        return

    for i in range(br):
        # cnt +=1
        abc(level+1)

abc(0)

print(cnt)