T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    plan = list(map(int, input().split()))

    cost = [0]*15
    for i in range(12):
        if plan[i]*day <= month:
            cost[i] = plan[i]*day
        else:
            cost[i] = month

    for i in range(1, 12):
        if cost[i] == 0: continue
        t = cost[i-1] + cost[i] + cost[i+1]
        if t > three:
            cost[i-1] = three
            cost[i] = 0
            cost[i+1] = 0

    print(cost)