sugar = [3, 5]
n = int(input())
result = []

MIN = 21e9
flag = 0
for i in range(n//3 +1):
    for j in range(n//5 +1):
        if 3*i + 5*j == n:
            flag = 1
            SUM = i + j
            MIN = min(SUM, MIN)
if flag == 0:
    print(-1)
else: print(MIN)