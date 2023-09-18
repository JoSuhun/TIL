n = int(input())
arr = [(int(input()), i) for i in range(n)]

# 버블정렬 할 때, 정렬이 한번도 이뤄지지 않은 턴이 몇번째?
newarr = sorted(arr)

MAX = -1
for i in range(n):
    x = newarr[i][1] - i
    if x > MAX:
        MAX = x
print(MAX+1)