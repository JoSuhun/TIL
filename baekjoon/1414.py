import heapq
import sys
input = sys.stdin.readline
n = int(input())
lan_list = [list(input()) for _ in range(n)]

q = []
total = 0
for i in range(n):
    for j in range(n):
        temp = 0
        if 97 <= ord(lan_list[i][j]) <=122:
            temp = ord(lan_list[i][j])-96
        elif 65 <= ord(lan_list[i][j]) <=90:
            temp = ord(lan_list[i][j])-38
        total += temp
        if temp >0 and i!=j:
            heapq.heappush(q, (temp, i, j))

boss = [0]*n
for i in range(n):
    boss[i] = i

def findboss(mem):
    if mem == boss[mem]:
        return mem
    else:
        boss[mem] = findboss(boss[mem])
        return boss[mem]

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa != fb:
        boss[fb] = fa

used = 0
lan = 0

while q:
    use, start, end = heapq.heappop(q)
    if findboss(start) != findboss(end):
        union(start, end)
        used += use
        lan += 1
if lan == n-1:
    print(total-used)
else:
    print(-1)
