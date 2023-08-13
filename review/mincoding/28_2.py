n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

boss_idx = 0
baby_idx = []

for i in range(n):
    if arr[i][0] == 1:
        boss_idx = i
    if arr[0][i] == 1:
        baby_idx.append(i)

print(f'boss:{boss_idx}')
print('under:',end='')
print(*baby_idx)