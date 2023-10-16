n, m = map(int, input().split())
lst = list(range(1, n+1))
path = []
result = []
def make(start, now):
    global path
    if now == m:
        print(*path[:])
        return
    for i in range(start, n):
        path.append(lst[i])
        make(i, now+1)
        path.pop()
make(0, 0)
