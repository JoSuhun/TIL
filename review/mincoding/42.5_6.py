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
        elif abs(ord(arr[now]) - ord(arr[now+1])) >= 5:
            SUM += 3
        now+=1
    return SUM


MAX = -21e8
lst = []
backup = copy.deepcopy(words)
def change(now):
    global words, MAX, lst

    if now == n:
        ret = grade(words)
        lst.append(ret)
        words = backup
        return

    for i in range(len(words)):
        for j in range(len(words)):
            words[i],words[j] = words[j],words[i]
        change(now+1)


change(0)
print(max(lst))
