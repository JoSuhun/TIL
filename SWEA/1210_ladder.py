for tc in range(10):

    n = int(input())

    arrs = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]

    for i in range(100):
        if arrs[99][i] == 2:
            x = i
    
    y = 98
    while y >= 0:

        if arrs[y][x-1] == 1:
            while True:
                x-=1
                if arrs[y-1][x] == 1:
                    y-=1
                    break
        elif arrs[y][x+1] == 1:
            while True:
                x+=1
                if arrs[y-1][x] ==1:
                    y-=1
                    break
        else:
            y-=1
    
    print(x)
                
            