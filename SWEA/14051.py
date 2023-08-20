from collections import deque
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())    # 개수, 이동 횟수
    nums = list(map(int, input().split()))
    idx = m%n
    print(f'#{tc} {nums[idx]}')