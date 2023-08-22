T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # 깃발 크기 n * m
    flag = [list(input()) for _ in range(n)]
    for f in flag:
        print(*f)