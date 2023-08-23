num = int(input())
lst = [list(map(int,input().split())) for _ in range(num)]
result=[]


for j in range(6):
    if lst[0][j]!=6:
        side=[]
        top = j
        for i in range(num):
            bottom=top
            if bottom==0:   #a
                top = 5
                Max = 0
                for k in range(6):
                    if k == 5: continue
                    if k == 0: continue
                    # if k==1 or k==2 or k==3 or k==4:    #bcde
                    if lst[i][k]>Max:
                        Max = lst[i][k]
                side.append(Max)
            elif bottom==1: #b
                top = 3 #d
                Max = 0
                for k in range(6):
                    if k == 1: continue
                    if k == 3: continue
                    # if k == 0 or k == 2 or k == 4 or k == 5:#acdf
                    if lst[i][k] > Max:
                        Max = lst[i][k]
                side.append(Max)
            elif bottom==2: #c
                top = 4 #e
                Max = 0
                for k in range(6):
                    if k == 2: continue
                    if k == 4: continue
                    # if k == 0 or k == 1 or k ==3  or k == 5: #abdf
                    if lst[i][k] > Max:
                        Max = lst[i][k]
                side.append(Max)
            elif bottom==3: #d
                top = 1#b
                Max = 0
                for k in range(6):
                    if k == 3: continue
                    if k == 1: continue
                    # if k == 0 or k == 2 or k == 4 or k == 5: #acef
                    if lst[i][k] > Max:
                        Max = lst[i][k]
                side.append(Max)
            elif bottom==4: #e
                top = 2#c
                Max = 0
                for k in range(6):
                    if k == 2: continue
                    if k == 4: continue
                    # if k == 0 or k == 1 or k ==3  or k == 5: #abdf
                    if lst[i][k] > Max:
                        Max = lst[i][k]
                side.append(Max)
            elif bottom==5: #f
                top = 0 #a
                Max = 0
                for k in range(6):
                    if k == 5: continue
                    if k == 0: continue
                    # if k==1 or k==2 or k==3 or k==4: #bcde
                    if lst[i][k] > Max:
                        Max = lst[i][k]
                side.append(Max)
        print(side)

        result.append(sum(side))
        print(result)
print(max(result))
