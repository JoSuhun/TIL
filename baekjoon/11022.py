T=int(input())
arr=[list(map(int,input().split())) for i in range(T)]
for i in range(T):
    print(f'Case #{i+1}: {arr[i][0]} + {arr[i][1]} = {arr[i][0] + arr[i][1]}')