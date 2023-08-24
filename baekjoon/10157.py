c, r = map(int,input().split())     # 공연장 크기 // i = c * j = r
k = int(input())    # 타겟 관객 번호
arrs = [[0]*r for _ in range(c)]
cnt = 0

directy = [-1, 0, 1, 0]
directx = [0, 1, 0, -1]

if k > c*r:
    print(-1)

i = 0
y = r
x = 0
while k <= c*r:
    cnt += 1
    y += directy[i]
    x += directx[i]
    if y .. ...