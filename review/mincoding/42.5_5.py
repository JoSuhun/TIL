eat = list(map(int, input().split()))
n = int(input())
n_arr = [0]*3*n
used = [0]*3*n

def eating(SUM, num, turn, arr):

    if turn == n:
        print(SUM)
        print(n_arr)
        return

    if num == 1:
        for i in range(3):
            if used[i] == 1:
                eating(SUM, 2, turn, arr)
            else:
                used[i] = 1
                eating(SUM+arr[i], 2, turn, arr)

    if num == 2:
        for i in range(3,6):
            if used[i] == 1:
                eating(SUM, 3, turn, arr)
            else:
                used[i] = 1
                eating(SUM+arr[i], 3, turn, arr)

    if num == 3:
        for i in range(6):
            n_arr[i] = arr[i] * 2
        for i in range(1,5):
            if used[i] == 1:
                eating(SUM, 1, turn+1, n_arr)
            else:
                used[i] = 1
                eating(SUM+arr[i], 1, turn+1, n_arr)

eating(0, 1, 0, eat)
