def solution(stones, k):

    now = 0
    while True:
        cnt = 0
        for i in range(len(stones)):
            if cnt == k:
                break
            if stones[i] != 0:
                stones[i] -= 1
            else:
                cnt += 1

        now += 1
        if cnt >= k: break

    return now

stones = list(map(int, input()[1:-2].split(',')))
k = int(input())

ret = solution(stones,k)
print(ret)