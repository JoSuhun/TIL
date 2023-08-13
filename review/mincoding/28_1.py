name = ['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']
arr = [[0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0]]

MAX = -21e8
for j in range(5):
       SUM = 0
       for i in range(5):
              if arr[i][j] == 1:
                     SUM += 1
       if SUM > MAX:
              MAX = SUM
              MAX_idx = j
print(name[MAX_idx])