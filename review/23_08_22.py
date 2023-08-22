name = ' ABCDEFG'   # 이진트리 *2 // *2+1

# [1]전위순회
def preorder(now):
    if now > len(name)-1: return
    print(name[now], end=' ')

    preorder(now*2)
    preorder(now*2 +1)
preorder(1)     # A B D E C F G


print()


# [2]후위순회
def postorder(now):
    if now > len(name)-1: return

    postorder(now*2)
    preorder(now*2 +1)
    print(name[now], end=' ')
postorder(1)    # D E B C F G A


print()


# [3]중위순회
def inorder(now):
    if now > len(name)-1: return

    inorder(now*2)
    print(name[now], end=' ')
    inorder(now*2 +1)
inorder(1)      # D B E A F C G

print()




# ---------------------------------------------------------------

# BST (binary search tree)

# 왼쪽 자식 노드에는 부모보다 작은 값, 오른쪽 자식 노드에는 부모보다 큰 값을 넣는다.
# 평균 logN의 속도로 저장하고 탐색하는 자료구조이다.
# 입력되는 데이터에 따라서 최악의 경우 O(n)의 속도가 될 수 있다.
# 이 때에는 Balanced tree로 만들어주는 알고리즘을 사용하면 logN에 가까운 속도로 탐색할 수 있다.
# Balanced tree로 만들어주는 대표적인 알고리즘으로는, red-black tree와 B-tree가 있다.

lst = [4, 2, 9, 1, 15, 3]
arr = [0] * 20

def insert(target):
    now = 1     # index
    while 1:
        if arr[now] == 0:
            arr[now] = target
            return

        if arr[now] < target:
            now = now*2 + 1
        if arr[now] > target:
            now = now*2


# lst배열을 tree형태로 저장
for i in lst:
    insert(i)

# 숫자 하나 입력 받고, 그 숫자 존재 여부 출력
n = int(input())

def Search(target):
    now = 1
    while 1:
        if now >= 20: return 0      # 배열 범위 벗어나면 안된다
        if arr[now] == 0: return 0

        if arr[now] == target:
            return 1
        if arr[now] < target:
            now = now*2 +1
        else: now = now*2

ans = Search(n)
if ans: print('찾음')
else: print('없음')




# ---------------------------------------------------------------

# heap

# max heap
arr = [6, 4, 1, 2, 6, 4, 8, 43]
heap = [0]*30
hindex = 1      # 1번 인덱스부터 값 넣기

def insert(value):
    global hindex
    heap[hindex] = value
    now = hindex
    hindex += 1

    while 1:
        p = now // 2    # 부모 인덱스 구하기
        if p == 0: break
        if heap[p] >= heap[now]: break      # 부모 값이 방금 들어온 값보다 크면 break
        heap[p], heap[now] = heap[now], heap[p]     # 부모 값이 방금 들어온 값보다 작으면 swap
        now = p        # 그 다음 부모가 now가 됨 (부모의 부모랑 또 비교)

def top():
    return heap[1]

def pop():
    global hindex
    hindex -= 1
    heap[1] = heap[hindex]
    heap[hindex] = 0

    now = 1
    while 1:
        son = now * 2
        rson = son + 1

        if rson <= hindex and heap[son] < heap[rson]: son = rson
        if son > hindex or heap[now] > heap[son]: break
        heap[now], heap[son] = heap[son], heap[now]
        now = son

for i in range(len(arr)):   # 이진트리 만들기
    insert(arr[i])

for i in range(len(arr)):
    print(top(), end=' ')    # 우선 순위가 가장 높은 것을 출력하는 함수
    pop()           # 출력 후 빼오기