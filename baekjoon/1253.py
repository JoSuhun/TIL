n = int(input())
arr = list(map(int, input().split()))
arr.sort()
flag = 0
cnt = 0

for target in range(n):
    start = 0
    end = n-1
    while start < end:
        if arr[start] + arr[end] == arr[target]:
            if start != target and end != target:
                cnt += 1
                break
            elif start == target:
                start += 1
            elif end == target:
                end -= 1
        elif arr[start] + arr[end] > arr[target]:
            end -= 1
        elif arr[start] + arr[end] < arr[target]:
            start += 1


print(cnt)
