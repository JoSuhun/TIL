import heapq
n = int(input())
MAX = []
MIN = []

for i in range(n):
    n = int(input())
    if n > 0: heapq.heappush(MAX, -n)
    else: heapq.heappush(MIN, n)

SUM = 0
while len(MIN)>1:
    a = heapq.heappop(MIN)
    b = heapq.heappop(MIN)
    SUM += a*b


while len(MAX)>1:
    a = -heapq.heappop(MAX)
    b = -heapq.heappop(MAX)
    if b==1:
        SUM += a
        heapq.heappush(MAX, -b)
    else: SUM += a*b

if MIN:
    SUM += MIN[0]
if MAX:
    SUM += -MAX[0]
print(SUM)