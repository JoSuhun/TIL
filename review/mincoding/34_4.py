n = int(input())    # n*n

cloud = [list(input()) for _ in range(n)]

def searchy(st, ed):
    y = -1
    while 1:
        md = (st + ed) // 2

        if cloud[md][0] == '0':
            ed = md-1
        elif cloud[md][0] == '#':
            y = md
            st = md+1
        if st>ed: break
    return y

def search(st, ed, y):
    x = -1
    while 1:
        md = (st + ed) // 2

        if cloud[y][md] == '0':
            ed = md-1
        elif cloud[y][md] == '#':
            x = md
            st = md+1
        if st>ed: break
    return x

yy = searchy(0, 7)
xx = search(0, 7, yy)
print(yy, xx)