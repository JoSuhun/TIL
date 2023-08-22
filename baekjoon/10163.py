n = int(input())    # 색종이 수

arrs = [[0]*1001 for _ in range(1001)]

def make(stx, sty, xlen, ylen, k):
    for i in range(stx, stx+xlen):
        for j in range(sty, sty+ylen):
            arrs[i][j] = k
    return arrs

for k in range(1, n+1):
    stx, sty, xlen, ylen = map(int, input().split())
    make(stx, sty, xlen, ylen, k)

for k in range(1, n+1):
    SUM = 0
    for i in range(1001):
        for j in range(1001):
            if arrs[i][j] == k:
                SUM += 1
    print(SUM)
