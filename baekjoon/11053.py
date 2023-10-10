n = int(input())
lst = list(map(int, input().split()))

result = [1] * n
for y in range(n):
    target = lst[y]
    for x in range(y):
        value = lst[x]
        if target > value:
            result[y] = max(result[x]+1, result[y])

print(max(result))