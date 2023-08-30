# # mst ... minimum spanning tree ...
# # union find
# # 독립된 데이터를 그룹화 ...
# # 문자 2개 입력 받고, 두 문자가 같은 그룹인지 판별
# arr = [0]*200
#
#
# def findboss(mem):
#     global arr
#     if arr[ord(mem)] == 0:
#         return mem
#     ret = findboss(arr[ord(mem)])
#     return ret
#
#
#
# def union(a, b):
#     global arr
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb: return
#
#     arr[ord(fb)] = fa
#
#
# union('a','b')
# union('d','e')
# union('b','e')
# union('b','d')
# union('e','f')
#
# y, x = input().split()
# if findboss(y) == findboss(x):
#     print('같은 그룹')
# else:
#     print('다른 그룹')




# # MST
# # 최소한의 간선으로 연결시킨 그래프
#
#
# n, m = map(int, input().split())
# edge = []
# for _ in range(m):
#     edge.append(input().split())
#
# # cycle 발견 출력 또는 cycle 미발견 출력하기
#
# arr = [0]*200
#
# def findboss(mem):
#     global arr
#     if arr[ord(mem)] == 0:
#         return mem
#     ret = findboss(arr[ord(mem)])
#     arr[ord(mem)] = ret
#     return ret
#
# def union(a, b):
#     global arr
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return 1
#     arr[ord(fa)] = fb
#
# ans = 0
# for i in range(m):
#     a, b = edge[i]
#     ret = union(a,b)
#     if ret == 1:
#         ans = 1
#         break
# if ans == 1: print('cycle 발견')
# else: print('미미미')


# kruskal

n,m=map(int,input().split())
lst=[list(input().split()) for _ in range(m)]
group=[0]*200
lst.sort(key=lambda x:int(x[2]))

def findboss(a):
    if not group[ord(a)]:
        return a
    ret=findboss(group[ord(a)])
    group[ord(a)]=ret
    return ret

def union(x,y,i):
    global group,total,cnt
    x_boss,y_boss=findboss(x),findboss(y)
    if x_boss==y_boss:
        return
    cnt+=1
    total+=int(lst[i][2])
    group[ord(y_boss)]=x_boss

total=0  # 총 공사비용
cnt=0   # 연결시킨 선의 개수

for i in range(m):
    if cnt==n-1:
        print(total)
        break
    union(lst[i][0],lst[i][1],i)


