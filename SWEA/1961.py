n = int(input())
arrs = [list(map(int, input().split())) for _ in range(3)]
print(arrs)

result = list([0]*3 for _ in range(3))
n_arrs = list([0]*3 for _ in range(3))
print(n_arrs)


for i in range(3):
    for j in range(3):
        n_arrs[i][j] = arrs[2-j][i]
print(n_arrs)