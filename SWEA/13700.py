# 이진탐색
# n 입력
# n 개의 정수 입력
# 찾고자 하는 target 1개 입력

n = int(input())
arr = list(map(int, input().split()))
target = int(input())


def binary_serch(start, end, target):

    while 1:

        mid=(start+end)//2

        if arr[mid] == target: return 1
        elif arr[mid] > target: end = mid-1
        elif arr[mid] < target: start = mid+1
        
        if start > end: return 0


arr.sort()

ans = binary_serch(0, n-1, target)  # 0은 시작인덱스, n-1은 arr배열의 마지막 인덱스

if ans: print('찾음')
else: print('못찾음')