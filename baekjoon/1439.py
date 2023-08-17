arr = list(map(int, input()))
n = len(arr)

cnt_0 = 0
cnt_1 = 0
if arr[0] == 1:
    cnt_1 += 1
else:
    cnt_0 += 1

start = 1

while start < n:
    if arr[start] == 0:
        if arr[start-1] != 0:
            cnt_0 += 1
    else:
        if arr[start-1] != 1:
            cnt_1 += 1

    start+=1

print(min(cnt_0, cnt_1))