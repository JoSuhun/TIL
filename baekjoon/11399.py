n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ret = 0
for i in range(1, n+1):
    ret += sum(lst[:i])
print(ret)