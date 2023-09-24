n = int(input())
k = int(input())
start = 1
end = k
ans = 0
while start <= end:
    mid = (start+end)//2
    ret = 0
    for i in range(1, n+1):
        if mid//i >= n:
            ret += n
        else:
            ret += mid//i
    if ret >= k:
        ans = mid
        end = mid-1
    else:
        start = mid+1

print(ans)