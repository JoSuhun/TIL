king, stone, n = map(str, input().split())
n=int(n)
king_y = int(king[1])-1
king_x = ord(king[0])-65

stone_y = int(stone[1])-1
stone_x = ord(stone[0])-65

print(king_y,king_x)
print(stone_y,stone_x)

def move(msg):
    global king_y, king_x, stone_y, stone_x
    if msg == 'R':
        king_x += 1
        if king_x > 7: pass
        if king_x == stone_x:
            stone_x += 1
            if stone_x > 7: pass
    if msg == 'L':
        king_x -= 1
        if king_x <0: pass
        if king_x == stone_x:
            stone_x -= 1
            if stone_x <0: pass
    if msg == 'B':
        
