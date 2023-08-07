T = int(input())

for tc in range(1, T+1):
    arrs = [list(map(str, input())) for _ in range(5)]

    MAX = -21e8
    for arr in arrs:
        if len(arr) > MAX:
            MAX = len(arr)

    n_arrs = []

    for j in range(MAX):
        for i in range(5):
            try:
                n_arrs.extend(arrs[i][j])
            except:
                continue

    print(f"#{tc} {''.join(n_arrs)}")

#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x