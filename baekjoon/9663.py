n = int(input())
board = [[0]*n for _ in range(n)]
cnt = 0
visit = [0]*n
def find(now):
    global cnt
    if now == n:
        cnt += 1
        return