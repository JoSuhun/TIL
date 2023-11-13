from collections import deque
n = int(input()) # 노드 개수
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    start, end, cost = map(int, input().split())
    tree[start].append((end, cost))
    tree[end].append((start, cost))
def find(now):
    q = deque()
    MAX = -1
    visit= [0]*(n+1)
    q.append(([now, 0]))
    while q:
        now, SUM = q.popleft()
        if SUM > MAX:
            MAX = SUM
        visit[now] = 1
        for next in tree[now]:
            if visit[next[0]]==1:continue
            q.append((next[0], SUM+next[1]))
    return MAX

ans = -1
for i in range(1, n+1):
    ret = find(i)
    ans = max(ans, ret)
print(ans)
