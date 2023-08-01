import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

m_lst = []
for _ in range(M):
    m_lst.append(list(map(int, input().split())))

for m in m_lst:
    print(sum(nums[m[0]-1:m[1]]))

## 런타임 오류