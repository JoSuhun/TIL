arr = [list(map(int, input().split())) for _ in range(4)]


def find(s, e, a):
    flag = 1
    for i in range(s, e, a):
        for j in range(s+1, e, a):
            if arr[i][j] == 1:
                print(f'({i},{j})')
                flag = 0
                break
        if flag == 0: break

find(0, 4, 1)
find(3, -1, -1)
