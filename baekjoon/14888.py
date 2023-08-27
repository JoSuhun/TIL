import copy
n = int(input())    # 수의 개수
numbers = list(map(int, input().split()))  # 수
p, m, mul, div = map(int, input().split())

MAX = -1e10
MIN = 1e10
def dfs(now, ret):
    global MAX, MIN, p, m, mul, div
    if now == n:
        MAX = max(MAX, ret)
        MIN = min(MIN, ret)
        return
    else:
        if p>0:
            p -= 1
            dfs(now+1, ret+numbers[now])
            p += 1
        if m>0:
            m -= 1
            dfs(now+1, ret-numbers[now])
            m += 1
        if mul > 0:
            mul -= 1
            dfs(now+1, ret * numbers[now])
            mul += 1
        if div > 0:
            div -= 1
            if ret < 0:
                dfs(now+1, -1* (abs(ret)//numbers[now]))
            else:
                dfs(now+1, ret//numbers[now])
            div += 1


dfs(1, numbers[0])
print(MAX)
print(MIN)
