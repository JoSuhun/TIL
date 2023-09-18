# # 분할 정렬
# arr = [2, 7, 5, 3, 1, 5, 9, 2]
# result = [0]*8
#
# def merge(start, end):
#     global arr, index, result
#     mid = (start+end)//2
#
#     if start >= end: return
#
#
#
#     merge(start, mid)
#     merge(mid+1, end)
#
#     a = start
#     b = mid+1
#     index = 0
#     while True:
#         if a>mid and b>end: break
#
#         if a>mid:
#             result[index] = arr[b]
#             index += 1
#             b += 1
#         elif b>end:
#             result[index] = arr[a]
#             index += 1
#             a += 1
#         elif arr[a] <= arr[b]:
#             result[index] = arr[a]
#             a += 1
#             index += 1
#         else:
#             result[index] = arr[b]
#             b += 1
#             index += 1
#
#     for i in range(index):
#         arr[start+i] = result[i]
#
# merge(0, 7)
# print(*result)



# # 병합정렬
# # 중간 기준으로 앞4, 뒤4 개의 숫자들은 오름차순 정렬을 전제
#
# lst = [2, 3, 5, 6, 1, 2, 8, 9]
# result = [0]*8
#
# start = 0
# end = 7
# mid = (start+end)//2
#
# a = start
# b = mid+1
#
# index = 0   # result 배열의 index 역할을 할 거다
#
# while True:
#     if a > mid and b > end: break
#
#     # a가 경계될 때, b가 경계될 때
#     if a > mid:
#         result[index] = lst[b]
#         b += 1
#     elif b > end:
#         result[index] = lst[a]
#         a += 1
#
#     elif lst[a] < lst[b]:
#         result[index] = lst[a]
#         a += 1
#     else:
#         result[index] = lst[b]
#         b += 1
#
#     index += 1
#
# print(result)

# ------------------------------------------------------------------------------------

# \( ^ o ^)/
# pivot

arr = [4, 1, 7, 9, 6, 3, 3, 6]
# pivot = arr[0]
#
# a = 1
# b = len(arr)-1
#
# while True:
#     while a < len(arr) and arr[a] <= pivot:
#         a += 1
#     while b >= 0 and arr[b] > pivot:
#         b -= 1
#     if a>b: break
#
#     arr[a], arr[b] = arr[b], arr[a]
# arr[0], arr[b] = arr[b], arr[0]
# print(arr)


# # quick 정렬
# def quick(start, end):
#     if start >= end: return
#
#     pivot = start
#     a = start + 1
#     b = end
#
#     while True:
#         while a <= end and arr[a] <= arr[pivot]:
#             a += 1
#         while b >= 0 and arr[b] > arr[pivot]:
#             b -= 1
#         if a>b: break
#         arr[a], arr[b] = arr[b],arr[a]
#     arr[pivot], arr[b] = arr[b], arr[pivot]
#
#
#     quick(start, b-1)
#     quick(b+1, end)
#
# quick(0, 7)
# print(arr)

# heapq / priority queue
import heapq

arr = [234, 454,26,3,1,45,67,2]

# heapq.heapify(arr)
#
# while arr:
#     ret = heapq.heappop(arr)
#     print(ret)

# maxheap으로 바꾸깅

heap = []
# [1]
# for i in range(len(arr)):
#     heapq.heappush(heap, -arr[i])
#
# while heap:
#     ret = -1 * heapq.heappop(heap)
#     print(ret)

# # [2]
# for i in range(len(arr)):
#     heapq.heappush(heap, (-arr[i], arr[i]))
#
# while heap:
#     ret = heapq.heappop(heap)[1]
#     print(ret)
#
# # [3]
#
# heap = list(map(lambda  x: -x, arr))
# heapq.heapify(heap)
#
# for i in range(len(arr)):
#     print(-heapq.heappop(heap))
# import heapq
# n = int(input())
# lst = [int(input()) for _ in range(n)]
# heapq.heapify(lst)
#
# SUM = 0
# while len(lst)>1:
#
#     card = heapq.heappop(lst)
#     card2 = heapq.heappop(lst)
#     SUM += (card + card2)
#     heapq.heappush(lst, card+card2)
#
# print(SUM)


# dijkstra ( n^2 버전 )

name = 'ABCDE'
inf = int(21e8)
arr = [[0, 3, inf, 9, 5],
        [inf, 0, 7, inf, 1],
        [inf, inf, 0, 1, inf],
        [inf, inf, inf, 0, inf],
        [inf, inf, 1, inf, 0]]

used = [0]*5
used[0] = 1
result = [0, 3, inf, 9, 5]

def select_ky():
    Min = int(21e8)
    MinIndex = 0
    for i in range(5):
        if used[i] == 0 and result[i] < Min:
            Min = result[i]
            MinIndex = i
    return MinIndex

def dijkstra():
    # 경유지 선택
    for i in range(4):
        via = select_ky()
        used[via] = 1

        # 시작점 -> 도착점 바로 / 시작점 -> 경유지 -> 도착점 /// 비교 후 최소비용을 result에 갱신
        for j in range(5):
            baro = result[j]
            kyung = result[via] + arr[via][j]
            if baro > kyung:
                result[j] = kyung

dijkstra()
print(*result)