from collections import deque

n = int(input())    # 맵 크기 n*n
arrs = [list(map(str, input())) for _ in range(n)]
# A 소화기 // $ 불 // # 벽
sty, stx = map(int, input().split())

