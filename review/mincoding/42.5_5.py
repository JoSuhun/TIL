n = int(input()) # cube n*n
cube = [list(map(int, input().split())) for _ in range(n)]

def makeCube(lst):  # 한 줄 씩 돌려서 나올 수 있는 경우 구하기
    result = []
    for i in range(n):
        path = [0]*n
        for j in range(n):
            path[j] = lst[(i+j)%n]
        result.append(path)
    return result

cube_lst = []
for c in cube:
    ret = makeCube(c)
    cube_lst.append(ret)


def grade(lst):     # 최종 점수 구하기
    gob = 1
    for j in range(n):
        SUM = 0
        for i in range(n):
            SUM += lst[i][j]
        gob *= SUM
    return gob


path = [' ']*n
MAX = -21e8
def dfs(now):       # 큐브를 돌려서 나올 수 있는 조합 구하기
    global MAX
    if now == n:
        ret = grade(path[:])
        if ret > MAX:
            MAX = ret
        return

    for i in range(n):
        path[now] = cube_lst[now][i]
        dfs(now+1)
dfs(0)
print(f'{MAX}점')
