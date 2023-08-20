import copy
words = list(input())
n = int(input())


def grade(arr):
    SUM = 0
    now = 0
    while now < len(arr)-1:
        if arr[now] == arr[now+1]:
            SUM -= 50
        elif abs(ord(arr[now]) - ord(arr[now+1])) >= 20:
            SUM += 10
        elif abs(ord(arr[now]) - ord(arr[now+1])) <= 5:
            SUM += 3
        now+=1
    return SUM


MAX = -21e8
lst = []
path = words[:]
def change(now):
    global MAX, lst, path

    if now == n:
        ret = grade(path)
        lst.append(ret)
        path = words[:]
        return

    for i in range(len(words)):
        for j in range(i, len(words)):
            path[i],path[j] = path[j],path[i]
            change(now+1)


change(0)
print(max(lst))
