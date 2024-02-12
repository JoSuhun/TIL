# 폰켓몬
nums = [3,3,3,2,2,2]
def solution(nums):
    answer = len(nums)/2
    used = set()
    for num in nums:
        used.add(num)
    return min(answer, len(used))

print(solution(nums))