import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    heapq.heappush(tree, (cost, start, end))

boss = [0]*(n+1)
for i in range(n+1):
    boss[i] = i

def findboss(mem):
    if boss[mem] == mem:
        return mem
    else:
        boss[mem] = findboss(boss[mem])
        return boss[mem]

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    boss[fb] = fa


total = 0
last = 0

while tree:
    cost, a, b = heapq.heappop(tree)
    if findboss(a) != findboss(b):
        union(a, b)
        total += cost
        last = cost

print(total-last)
