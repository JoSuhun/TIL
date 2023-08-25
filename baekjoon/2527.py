for _ in range(4):  # tc 4개
    arrs = [[0]*1000 for _ in range(1000)]
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if q2<y1 or q1<y2 or p1<x2 or p2<x1:
        ret = 'd'
    elif x1 == p2 or p1 == x2 or y1 == q2 or q1 == y2:
        ret = 'b'
        if (x1 == p2 and q1 == y2) or (p1 == x2 and y1 == q2) or (y1 == q2 and x1 == p2) or (q1 == y2 and p1 == x2):
            ret = 'c'
    else: ret = 'a'

    print(ret)