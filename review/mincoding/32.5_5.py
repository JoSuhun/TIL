idx = int(input())

arrs = [3, 2, -1, 3, -2, 'x', -1]

def find(idx, target):
    if idx == target:
        print(f'{idx}번')
        return

    find(idx+arrs[idx], target)
    print(f'{idx}번')

find(idx, 5)