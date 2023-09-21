import heapq

n = int(input())
lst = list(map(int, input().split()))
heapq.heapify(lst)
def isPrime(num):
    arr = [1]*num

    for i in range(2, int(num**0.5)+1):

        if arr[i] == 1:
            for j in range(i+i, num, i):
                arr[j] = 0
    if num>5:
        return sum(arr[6:])
    else:
        return 0

cnt = 0
while lst:
    x = heapq.heappop(lst)
    x += cnt
    cnt = isPrime(x)

    print(x+cnt, end=' ')