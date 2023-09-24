n, m = map(int, input().split())
# 나무의 수 n // 가져갈 나무 길이 m
trees = list(map(int, input().split()))

trees.sort()
start = 1
end = trees[-1]
ans = 0
while start <= end:
    mid = (start + end)//2
    SUM = 0
    for t in trees:
        if t < mid: continue
        SUM += (t-mid)
    if SUM < m:
        end = mid-1
    elif SUM >= m:
        start = mid+1
        ans = mid
print(ans)