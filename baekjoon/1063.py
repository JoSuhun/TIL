king, stone, n = map(str, input().split())
n=int(n)
king_y = int(king[1])-1
king_x = ord(king[0])-65

stone_y = int(stone[1])-1
stone_x = ord(stone[0])-65

dic = {'R':(0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0), 'RT':(1,1), 'LT':(1,-1), 'RB':(-1,1),'LB':(-1,-1)}


for _ in range(n):
    msg = input()

    i, j = dic[msg][0], dic[msg][1]

    if king_y + i <0 or king_y + i >7 or king_x + j <0 or king_x + j >7: continue
    if king_y + i == stone_y and king_x + j == stone_x:
        if stone_y +i <0 or stone_y +i >7 or stone_x +j <0 or stone_x + j>7: continue
        else:
            king_y += i
            king_x += j
            stone_y += i
            stone_x +=j
    else:
        king_y += i
        king_x += j

print(chr(king_x+65)+str(king_y+1))
print(chr(stone_x+65)+str(stone_y+1))