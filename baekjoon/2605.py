n = int(input())    # 학생 수
nums = list(map(int, input().split()))      # 뽑은 번호

q = []
student = 1
idx = 0
while student <= n:
    q.insert(len(q) - nums[student-1], student)
    student += 1
print(*q)