import sys
sys.setrecursionlimit(10**6)
def dfs(mem):
    global cnt
    visit[mem] = 1
    team.append(mem)
    print(team)
    if not visit[choice[mem]]:
        dfs(choice[mem])
    else:
        if choice[mem] in team:
            cnt += len(team[team.index(choice[mem]):])

T = int(input())
for tc in range(T):
    n = int(input())
    choice = [0]+list(map(int, input().split()))
    visit = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            team = []
            dfs(i)

    print(n-cnt)