def find(num):
    ret = 0
    a = 2
    while a<=int(num**0.5):
        if num % a == 0:
            ret += 1
            num = num//a
        else:
            a += 1
    if num != 1:
        ret += 1
    return ret
print(find(12))


a, b = map(int, input().split())
cnt = 0
arr = [1]*(b+1)
used = [0]*(b+1)

m = int(b**0.5)
for i in range(2, m+1):
    if used[i] == 1:
        continue
    if arr[i] == 1:
        for j in range(i+i, b+1, i):
            used[j] = 1
            arr[j] = 0

for i in range(a, b+1):
    x = find(i)
    if x>1 and arr[x] == 1:
        cnt += 1
print(cnt)