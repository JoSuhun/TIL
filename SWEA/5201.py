T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())    # n 컨테이너 // m 트럭
    nlst = list(map(int, input().split()))
    mlst = list(map(int, input().split()))

    MAX = -1
    used = [0]*n
    path = []
    def choice(now, start, SUM):
        global MAX
        if now == min(n,m):
            MAX = max(MAX, SUM)
            return

        for i in range(start, m):
            for j in range(n):
                if nlst[j]>mlst[i]: continue
                if used[j] == 1: continue
                used[j] = 1
                path.append(nlst[j])
                choice(now+1, i+1, SUM+nlst[j])
                used[j] = 0

    choice(0,0,0)
    print(MAX)