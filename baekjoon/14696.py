n = int(input())    # n 라운드 수

def findCard(arr1, arr2):
    for i in range(4, 0, -1):
        if arr1.count(i) > arr2.count(i):
            winner = 'A'
            break
        elif arr1.count(i) < arr2.count(i):
            winner = 'B'
            break
    if arr1 == arr2:
        winner = 'D'
    return winner

for _ in range(n):
    a = list(map(int, input().split()))
    a_n = a.pop(0)
    b = list(map(int, input().split()))
    b_n = b.pop(0)
    a.sort()
    b.sort()

    ret = findCard(a, b)
    print(ret)