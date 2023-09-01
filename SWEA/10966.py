from collections import deque
T = int(input())

def find(sty, stx, edy, edx, now):





for tc in range(1, T+1):
    n, m = map(int, input().split())
    arrs = [list(input()) for _ in range(n)]

    q = deque()

    endlst = []
    for i in range(n):
        for j in range(m):
            if arrs[i][j] == 'W':
                endlst.append((i,j))
