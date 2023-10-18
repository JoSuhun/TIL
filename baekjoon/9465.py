T = int(input())
for tc in range(T):

    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append([0,0]+list(map(int, input().split())))

    for j in range(2, n+2):
        stickers[0][j] += max(stickers[0][j-2], stickers[1][j-2], stickers[1][j-1])
        stickers[1][j] += max(stickers[0][j-2], stickers[0][j-1], stickers[1][j-2])
    print(max(max(stickers[0]), max(stickers[1])))