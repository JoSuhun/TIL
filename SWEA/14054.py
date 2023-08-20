from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n 화덕크기, m 피자 개수
    pizza = list(map(int, input().split()))

    q = deque()
    for i in range(n):
        q.append((pizza[i], i+1))

    now = n
    while len(q)>1:
        a, idx = q.popleft()
        if a//2 > 0: q.append((a//2, idx))
        else:
            if now<m:
                q.insert(0,(pizza[now], now+1))
                now += 1
            else: continue

    MAX = -21e8
    MAX_idx = 0
    for lst in q:
        if lst[0] > MAX:
            MAX = lst[0]
            MAX_idx = lst[1]
    print(f'#{tc} {MAX_idx}')
