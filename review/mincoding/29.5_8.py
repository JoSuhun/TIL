arr = [list(input()) for _ in range(4)]
print(arr)
def move(y, x):

    direct_y = [0, -1, 0, 1, 0]
    direct_x = [1, 0, -1, 0, 1]
    for i in range(5):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 2: continue
        if arr[dy][dx] != '_': continue
        arr[y][x], arr[dy][dx] = arr[dy][dx], arr[y][x]

        move(dy, dx)

move(2, 1)

print(arr)




