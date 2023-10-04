from collections import deque
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def make(start):
    q = deque()
    q.append(start)
    visit[start] = 1
    while q:
        now= q.popleft()

        for next in lst[now]:
            if visit[next[0]] == 1: continue
            visit[next[0]] = 1
            result[next[0]] = result[now]*next[2]//next[1]
            q.append(next[0])

n = int(input())
lst = [[] for _ in range(n)]
gcm = 1
for i in range(n-1):
    s, e, p, q = map(int, input().split())
    lst[s].append((e, p, q))
    lst[e].append((s, q, p))
    gcm *= (p*q)//gcd(p, q)


visit = [0]*n
result = [0]*n
result[0]=gcm
make(0)
xgcm = result[0]

for i in range(1, n):
    xgcm = gcd(xgcm, result[i])

for i in range(n):
    print(result[i]//xgcm, end=' ')