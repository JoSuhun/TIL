T = int(input())

def make(num):
    num = int(num)
    arr = [0]*4
    n = 3
    while n >= 0:
        arr[n] = str(num%2)
        num = num//2
        n-=1
    return arr


for tc in range(1, T+1):
    n, lst = map(str, input().split())
    n = int(n)
    lst = list(lst)
    ans = []
    for i in range(n):
        if 65<= ord(lst[i]) <=70:
            ret = make(ord(lst[i])-55)
        else:
            ret = make(lst[i])
        ans.extend(ret)
    print(f"#{tc} {''.join(ans)}")