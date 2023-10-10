n, m = map(int, input().split())
cnt = 0
strs = []
for _ in range(n):
    strr = input()
    strs.append(strr)
    cnt += len(strr)
a, b = divmod(m-cnt, n-1)

ans = [strs[0]]
for i in range(1, n):
    if (strs[i][0].islower() and b >0) or i+b == n:
        ans.append('_'*(a+1)+strs[i])
        b -=1
    else:
        ans.append('_'*a+strs[i])
print(''.join(ans))
