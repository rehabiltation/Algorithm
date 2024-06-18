# 소요시간: 4분
# 특이사항: 처음에 for i in range(M, N+1)로 했다가 어케할줄 몰라서 바꿨어염

M = int(input())
N = int(input())
nums = []

for i in range(1, 101):
    if M <= i**2 <= N:
        nums.append(i**2)

if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)