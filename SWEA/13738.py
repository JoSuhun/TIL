T = int(input())

for tc in range(1, T+1):

    str1 = list(input())
    str2 = list(input())

    N = len(str1)
    M = len(str2)

    def isSame():
        for i in range(M-N+1):
            cnt = 0
            for j in range(N):
                if str2[i+j] == str1[j]:
                    cnt += 1
            if cnt == N:
                return 1
        return 0

    ret = isSame()
    
    print(f'#{tc} {ret}')
