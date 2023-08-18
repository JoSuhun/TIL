
# 소화기에서 -> 사람 (배열범위x 중복체크x 벽x 불x)
# 소화기에서 -> 불 (배열범위x 중복체크x 벽x)
#
# for문 돌아서 소화기좌표 저장 그리고 소화기 개수 cnt
# 불의 좌표 저장
#
# 소화기 개수만큼 반복하고
# (소화기->사람) + (소화기->불) 더한 결과값의 최소값 출력
# BFS함수 내에서 type이 0이면 불 신경씀 type이 1이면 불은 신경안씀

from collections import deque

n=int(input())
arr=[list(input()) for _ in range(n)]
y,x=map(int,input().split())

sohwa=[]
so_Cnt=0
fy,fx=0,0

for i in range(n):
    for j in range(n):
        if arr[i][j]=='A':
            sohwa.append([i,j])
            so_Cnt+=1
        if arr[i][j]=='$':
            fy=i
            fx=j


def bfs(sty,stx,edy,edx,type):
    q=deque()
    q.append([sty,stx,0])
    visit=[[0]*n for _ in range(n)]
    visit[sty][stx]=1

    while q:
        nowy,nowx,level=q.popleft()
        directy=[0,0,-1,1]
        directx=[-1,1,0,0]
        for i in range(4):
            dy=directy[i]+nowy
            dx=directx[i]+nowx
            if dy<0 or dy>n-1 or dx<0 or dx>n-1: continue
            if visit[dy][dx]==1: continue
            if arr[dy][dx]=='#': continue
            if type==0 and arr[dy][dx]=='$': continue

            visit[dy][dx]=1
            q.append((dy,dx,level+1))

            if dy==edy and dx==edx:
                return level+1

Min=21e8
for i in range(so_Cnt):
    Min=min(Min,(bfs(sohwa[i][0],sohwa[i][1],y,x,0)+bfs(sohwa[i][0],sohwa[i][1],fy,fx,1)))
print(Min)