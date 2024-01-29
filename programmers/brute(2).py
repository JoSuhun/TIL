sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    answer = 0
    max_x = max(sizes[0])
    max_y = min(sizes[0])
    for i in range(1, len(sizes)):
        next = sizes[i]
        next_x = max(next)
        next_y = min(next)
        max_x = max(max_x, next_x)
        max_y = max(max_y, next_y)
    answer = max_x * max_y
    return answer
