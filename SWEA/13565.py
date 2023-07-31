for tc in range(10):
    n = int(input())
    box_h = list(map(int, input().split()))

    for _ in range(n):
        for i in range(100):
            if box_h[i] == min(box_h):
                box_h[i] += 1
                break
        for i in range(100):
            if box_h[i] == max(box_h):
                box_h[i] -= 1
                break

    print(f'{tc+1} {max(box_h) - min(box_h)}')
