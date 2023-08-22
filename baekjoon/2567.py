n = int(input())    # 색종이 수

arrs = [[0]*102 for _ in range(102)]    # 도화지

for _ in range(n):
    stx, sty = map(int, input().split())    # x 왼쪽 변 사이 거리 // y 아래쪽 변 사이 거리 // 색종이 크기 10*10
    stx += 1
    sty += 1
    edx = stx + 10
    edy = sty + 10

    for i in range(sty, edy):
        for j in range(stx, edx):
            arrs[i][j] = 1

result = 0
directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

for i in range(102):
    for j in range(102):
        if arrs[i][j] == 0:
            for k in range(4):
                dy = i +directy[k]
                dx = j + directx[k]
                if dy<0 or dx<0 or dy>101 or dx>101: continue
                if arrs[dy][dx] == 1: result += 1

print(result)
