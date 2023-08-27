n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
num = 1
ans = ''
result = 1
for i in range(n):
    now = nums[i]
    if now >= num:
        while now >= num:
            stack.append(num)
            num += 1
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    else:
        n = stack.pop()
        if n > now:
            print('NO')
            result = 0
            break
        else:
            ans += '-\n'
if result:
    print(ans)

