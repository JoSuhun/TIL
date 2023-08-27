s = int(input())
n = 1
SUM = 0
while True:
    SUM += n
    if SUM > s:
        n -= 1
        break
    n += 1
print(n)