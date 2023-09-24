n, m = map(int, input().split())
# n 강의 수 // m 블루레이 수
minutes = list(map(int, input().split()))

start = max(minutes)    # 블루레이 크기 최소, m = n
end = sum(minutes)      # 블루레이 크기 최대, m = 1

ans = 0
while start <= end:
    mid = (start+end)//2
    cnt = 1
    set = 0
    for i in minutes:
        if set + i > mid:
            cnt += 1
            set = 0
        set += i
    if cnt <= m:
        ans = mid
        end = mid - 1
    elif cnt > m:
        start = mid + 1

print(ans)