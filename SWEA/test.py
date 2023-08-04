map_lst = [[3,5,1], [3,8,1], [1,1,5]]

bitarray = []
for _ in range(2):
    bitarray.append(list(map(int, input().split())))


def masking(y,x):
    SUM = 0
    for i in range(2):
        for j in range(2):
            if bitarray[i][j] == 1:
                SUM += map_lst[y+i][x+j]
    return SUM


MAX = -21e8
MAX_y = 0
MAX_x = 0

for y in range(2):
    for x in range(2):
        ret = masking(y,x)
        if ret > MAX:
            MAX = ret
            MAX_y = y
            MAX_x = x

print(f'({MAX_y},{MAX_x})')