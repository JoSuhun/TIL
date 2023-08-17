arr = list(map(int, input()))
n = len(arr)
bucket = [0]*10

for i in range(n):
    if arr[i] == 6:
        bucket[9] +=1
    else:
        bucket[arr[i]] +=1

max_idx = bucket.index(max(bucket))
if max_idx == 9:
    print(max(bucket) - max(bucket)//2)
else:
    print(max(bucket))