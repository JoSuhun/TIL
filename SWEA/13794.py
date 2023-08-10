# def delete(arr):
#     end = len(arr)-1
#     while end>0:
#         for i in range(end):
#             if arr[i] == arr[i+1]:
#                 arr.pop(i)
#                 arr.pop(i)
#                 break
#         end-=2
#     return arr
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(input())
#     ret = delete(arr)
#     print(f'#{tc} {len(ret)}')
#


# STACK

T = int(input())

for tc in range(1, T+1):
    st = input()
    stack = []

    for s in st:
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')