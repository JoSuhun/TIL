# 부분집합 원소의 합들

def print_subset(bit, arr, n):
    total = 0   # 부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)

arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr, 4)




# 비트연산과 부분집합

arr = [3, 6, 7, 1, 5, 4]

n = len(arr)    # 원소의 개수 n

for i in range(1<<n):       # 부분집합의 개수 1<<n (2의 n승)
    for j in range(n):      # 원소의 수만큼 비트 비교
        if i & (1<<j):                   # i의 j번 비트가 1인 경우
            print(arr[j], end=', ')      # j번 원소 출력
    print()
print()


# ------------------------------------------------------------------

# arrs = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
# y,x = map(int, input().split())
#
# directy = [1, 0, 0, -1]
# directx = [0, 1, -1, 0]
#
# SUM = arrs[y][x]
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]
#
#     if dy<0 or dy>2 or dx<0 or dx>2: continue
#     SUM += arrs[dy][dx]
#
# print(SUM)

# 입력받은 좌표값의 대각선에 있는 값들의 곱 구하기
#
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# y,x = map(int, input().split())
#
# directy = [1, 1, -1, -1]
# directx = [1, -1, -1, 1]
#
# MUL = 1
# for i in range(4):
#     dy = y + directy[i]
#     dx = x + directx[i]
#
#     if dy<0 or dy>4 or dx<0 or dx>4: continue
#     MUL = MUL * arr[dy][dx]
#
# print(MUL)



# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# y,x = map(int, input().split())
#
# directy = [1, 0, 0, -1]
# directx = [0, 1, -1, 0]
#
# SUM = 0
# for i in range(4):
#     for j in range(1,4):
#         dy = y + directy[i]*j
#         dx = x + directx[i]*j
#         if dy<0 or dy>4 or dx<0 or dx>4: continue
#         SUM += arr[dy][dx]
# print(SUM)


# # +모양 합들 중에서 최대값을 구할거야
arr=[[1,2,3,4],
    [1,2,9,4],
    [1,9,3,9],
    [1,2,9,4]]



def isSum(y,x):

    directy = [1,-1,0,0]
    directx = [0,0,1,-1]

    SUM = 0

    for i in range(4):
        dy = y+ directy[i]
        dx = x + directx[i]
        if dy<0 or dy>3 or dx<0 or dx>3: continue
        SUM += arr[dy][dx]

    return SUM

MAX = -21e8
MAX_i = 0
MAX_j = 0

for i in range(4):
    for j in range(4):
        ret = isSum(i,j)
        if ret > MAX:
            MAX = ret
            MAX_i = i
            MAX_j = j

print(MAX, MAX_i, MAX_j)



arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

# 4*4 배열안의 값의 합을 구할 것입니다.
# for문으로 구한 후 출력해 주세요.

# sum1= 1+1+2+3+4+5 를 하면 출력은 16이 출력이 될 것이고
# sum2= 5+4+5+2+7+1 를 하면 출력은 24가 출력이 될 것입니다.

#sum1
# sum1 = 0
# for i in range(1,4):
#     for j in range(0,i):
#         sum1 += arr[i][j]
# print(sum1)
#
# #sum2
# sum2 = 0
# for i in range(0,3):
#     for j in range(i+1,4):
#         sum2 += arr[i][j]
# print(sum2)




arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]


sum3 = 0
sum4 = 0
for i in range(4):
        sum3 += arr[i][i]
        sum4 += arr[i][3-i]

print(sum3, sum4)


arr = [[3, 5, 4, 5],
       [1, 1, 2, 7],
       [1, 2, 9, 1],
       [3, 5, 4, 5]]

sum5 = [0]*7
for i in range(4):
    for j in range(4):
        sum5[i+j] += arr[i][j]
print(sum5)










