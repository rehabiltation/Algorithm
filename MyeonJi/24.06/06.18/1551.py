# 소요시간: 8분
# 특이사항: nums = new_nums 이거 생각하는게 오래걸림

N, K = map(int, input().split())
nums = list(map(int, input().split(',')))

for _ in range(K):
    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append(nums[i + 1] - nums[i])
    nums = new_nums  # 변형된 수열로 업데이트

print(','.join(map(str, nums)))
