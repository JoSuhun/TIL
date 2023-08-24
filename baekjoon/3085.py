# C, P, Z
# 인접 교환 1회 후, 가장 긴 연속 행 또는 열
n = int(input())
arrs = [list(input()) for _ in range(n)]


def isMAX(arrs):
    lst = []

    for i in range(n):
        r_cnt = 1
        c_cnt = 1
        for j in range(n-1):
            if arrs[i][j] == arrs[i][j+1]:
                r_cnt += 1
                lst.append(r_cnt)
            elif arrs[i][j] != arrs[i][j+1]:
                r_cnt = 1
            if arrs[j][i] == arrs[j+1][i]:
                c_cnt += 1
                lst.append(c_cnt)
            elif arrs[j][i] != arrs[j+1][i]:
                c_cnt = 1

    ret = max(lst)
    return ret


lst = []
for i in range(n):
    for j in range(n-1):
        arrs[i][j], arrs[i][j+1] = arrs[i][j+1], arrs[i][j]
        max1 = isMAX(arrs)
        lst.append(max1)
        arrs[i][j+1],arrs[i][j] = arrs[i][j],arrs[i][j+1]

for j in range(n):
    for i in range(n-1):
        arrs[i][j], arrs[i+1][j] = arrs[i+1][j], arrs[i][j]
        max2 = isMAX(arrs)
        lst.append(max2)
        arrs[i+1][j], arrs[i][j] = arrs[i][j], arrs[i+1][j]

print(max(lst))