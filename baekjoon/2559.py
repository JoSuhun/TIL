n, k = map(int, input().split())    # n 전체 날짜 수 // k 연속적인 날짜 수
lst = list(map(int, input().split()))
result = [0]
temp = 0

for i in lst:
    temp = temp + i
    result.append(temp)


MAX = -2128
for i in range(k, n+1):
    SUM = result[i] - result[i-k]
    if SUM > MAX:
        MAX = SUM
print(MAX)