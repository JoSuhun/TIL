n = int(input())

def isPrime(x):
    m = int(x**0.5)+1
    for i in range(2, m):
        if x % i == 0:
            return 0
    return 1

numlst = [2, 3, 5, 7]
def dfs(now, x):
    if now == n:
        print(x)
        return

    for i in range(10):
        if i%2 == 0: continue
        ret = x*10 + i
        if isPrime(ret):
            dfs(now+1, ret)


for i in range(4):
    x = numlst[i]
    dfs(1, x)