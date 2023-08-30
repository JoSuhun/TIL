# MST
# 최소한의 간선으로 연결시킨 그래프


n, m = map(int, input().split())
edge = []
for _ in range(m):
    edge.append(input().split())

# cycle 발견 출력 또는 cycle 미발견 출력하기

arr = [0]*200

ans = 0
for i in range(m):