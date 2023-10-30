n = int(input())    # 노드 개수
node = list(map(int, input().split()))
delete = int(input())

def find(delete):
    node[delete] = -2
    for i in range(n):
        if node[i] == delete:
            find(i)

find(delete)

cnt = 0
for x in range(n):
    if node[x] != -2 and x not in node:
        cnt += 1
print(cnt)