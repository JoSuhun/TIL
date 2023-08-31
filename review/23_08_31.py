# 위상정렬
# 작업 순서를 정할 때
from collections import deque

name=['cs','language','datastructure','algorithm','project','codingtest','beaprogrammer']
arr=[
    [0,0,0,0,0,0,1],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0]]

acc=[0]*7  # 사전 작업 개수

# 사전 작업 개수 등록
for j in range(7):
    for i in range(7):
        if arr[i][j]==1:
            acc[j]+=1
print(acc)

q=deque()
# 당장 사전작업 없이 착수할수 있는것 넣어주기
for i in range(7):
    if acc[i]==0:
        q.append(i)
print(q)
while q:
    now=q.popleft()
    print(name[now])
    for i in range(7):
        if arr[now][i]==1:  # 작업을 할 수 있을때
            if acc[i]==1:   # 작업개수가 1개 남았다면
                acc[i]-=1   # 작업개수 1뺴고 (사전 작업이 더이상 없고)
                q.append(i) # 사전작업이 다 없어 졌음으로 큐에 푸쉬
            else:
                acc[i]-=1   # 필요한 작업개수를 1개 감소