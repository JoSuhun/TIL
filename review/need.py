# 1 2 3 4 5
# 2 4 2 1 3
# 3 4 5 2 5
#
# 3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!
#
# 정답은:
# 0 2
# 2 0

arrs = [[1,2,3,4,5],[2,4,2,1,3],[3,4,5,2,5]]
pattern = [3,4,5]

def findPattern(y, x):
    for i in range(3):
        if pattern[i] != arrs[y][x+i]:
            return 0
    return 1

for i in range(3):
    for j in range(3):
        ret = findPattern(i,j)
        if ret: print(i,j)

## Counting 정렬
A = [4,7,1,4,2,4,3]

bucket = [0]*11

for a in A:
    bucket[a] += 1

print(bucket)

for i in range(len(bucket)-1):
    bucket[i+1]+=bucket[i]

print(bucket)

result = [0]*7

for i in range(len(A)):
    bucket[A[i]]-=1
    index=bucket[A[i]]
    result[index]=A[i]