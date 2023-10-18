import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for i in range(n):
    node, left, right = input().split()
    tree[node] = left, right

def preorder(now):
    if now == '.': return
    print(now, end='')
    preorder(tree[now][0])
    preorder(tree[now][1])
preorder('A')

print()
def inorder(now):
    if now == '.': return
    inorder(tree[now][0])
    print(now, end='')
    inorder(tree[now][1])
inorder('A')

print()
def postorder(now):
    if now == '.': return
    postorder(tree[now][0])
    postorder(tree[now][1])
    print(now, end='')
postorder('A')