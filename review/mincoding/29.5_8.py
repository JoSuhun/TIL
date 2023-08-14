arr = [list(input()) for _ in range(4)]

def findIdx(a):
    for i in range(4):
        for j in range(3):
            if arr[i][j] == a:
                return i, j
