N, K = map(int, input().split())
nums = list(map(int, input().split()))

current = sum(nums[:K])
max_sum = current

for i in range(K, N):
    current += nums[i] - nums[i - K]
    if current > max_sum:
        max_sum = current

print(max_sum)