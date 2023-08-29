card = list(input())
n = int(input())
card.sort()
card = card[-6::]
ans = sorted(card, key=lambda x: -card.count(x))
print(ans[0])