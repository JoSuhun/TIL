T = int(input())

for tc in range(1, T+1):

    arrs = [[0]*10 for _ in range(10)]
    N = int(input())

    for color in range(N):

        color_index = list(map(int, input().split()))

        for i in range(color_index[0], color_index[2]+1):
            for j in range(color_index[1], color_index[3]+1):
                arrs[i][j]+=1

    
    cnt =0
    for arr in arrs:
        for a in arr:
            if a ==2:
                cnt += 1
    
    print(f'#{tc} {cnt}')