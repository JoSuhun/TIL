heroes = ['B', 'I', 'A', 'H']
n = int(input())


def dfs(hero_idx, heroes):
    if len(heroes)==1:
        print(*heroes, end=' ')
        return
    print(heroes[hero_idx], end=' ')

    heroes.pop(hero_idx)

    next_idx = (hero_idx + n) % (len(heroes)) -1
    dfs(next_idx, heroes)

hero_index = n % len(heroes)-1
dfs(hero_index, heroes)
