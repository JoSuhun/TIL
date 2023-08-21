n, m = map(int, input().split())    # 블록의 가로 * 세로
n = int(input())    # 상점 개수
market = [list(map(int, input().split())) for _ in range(n)]    # 상점 위치// 1 북, 2 남, 3 서, 4 동 , 거리(위,왼)
dong = list(map(int, input().split()))
print(market, dong)

SUM = 0

lst =