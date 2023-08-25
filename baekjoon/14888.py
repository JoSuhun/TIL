import copy
n = int(input())    # 수의 개수
numbers = list(map(int, input().split()))  # 수
cnt = list(map(int, input().split()))
lst = ['+','-','x','%']
tool = []
for i in range(4):
    if cnt[i] == 0: continue
    for j in range(cnt[i]):
        tool.append(lst[i])



n_nums = copy.deepcopy(numbers)

def cal(nums, lst):
    while True:
        n1 = nums.pop(0)
        t1 = lst.pop(0)
        n2 = nums.pop(0)
        if t1 == '+':
            n3 = n1+n2
        elif t1 == '-':
            n3 = n1-n2
        elif t1 == 'x':
            n3 = n1*n2
        else:
            if n1 < 0:
                n3 = -1*(abs(n1)//n2)
            else: n3 = n1//n2
        nums.insert(0, n3)
        if len(lst) == 0: break
    ret = nums[0]
    return ret


path = [' '] * (n-1)
lst = []
used = [0]*(n-1)
MAX = -21e8
MIN = 21e8
def dfs(now):
    if now == n-1:
        lst.append(path[:])
        return
    for i in range(n-1):
        if used[i] == 1: continue
        used[i] = 1
        path[now] = tool[i]
        dfs(now+1)
        used[i] = 0
dfs(0)


MAX = -21e8
MIN = 21e8
for l in lst:
    ret = cal(numbers,l)
    MAX = max(MAX,ret)
    MIN = min(MIN,ret)
    numbers = copy.deepcopy(n_nums)
print(MAX)
print(MIN)
