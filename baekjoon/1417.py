N = int(input())

arr = [int(input()) for _ in range(N)]
if N == 1:
    print(0)
else:
    sort_arr = sorted(arr[1:])

    cnt = 0

    while True:
        if arr[0] > sort_arr[-1]: break
        arr[0] +=1
        sort_arr[-1] -=1
        sort_arr = sorted(sort_arr)
        cnt+=1


    print(cnt)