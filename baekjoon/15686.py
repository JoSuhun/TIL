from collections import deque
n, m = map(int, input().split())    # n*n 도시 // 치킨집 최대 m개
mapp = [list(map(int, input().split())) for _ in range(n)]

q = deque()