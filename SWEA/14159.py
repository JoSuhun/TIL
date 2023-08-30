# 0부터 9까지 숫자카드 * 4세트
T = int(input())


def makeRun(arr):
    cnt = 0
    for i in range(len(arr) - 1):
        if arr[i] + 1 == arr[i + 1]:
            cnt += 1
            if cnt >= 2:
                break
        elif arr[i] == arr[i+1]:
            continue
        else:
            cnt = 0
    if cnt >= 2:
        return 1
    else:
        return 0


def makeTriple(arr):
    cnt = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            cnt += 1
            if cnt >= 2:
                break
        else:
            cnt = 0
    if cnt >= 2:
        return 1
    else:
        return 0


for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    ans = 0
    for i in range(12):
        if i%2 == 0:
            player1.append(cards[i])
            player1.sort()
            if makeRun(player1) or makeTriple(player1):
                ans = 1
                break

        else:
            player2.append(cards[i])
            player2.sort()

            if makeRun(player2) or makeTriple(player2):
                ans = 2
                break
    print(f'#{tc} {ans}')


