# 소요시간:
# 특이사항: 리스트 안벗어나는 게 안떠오름

N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
ans = []
index = 0

while len(nums) != 0:
    index += K-1
    # 원형 구조를 만들기 위해 index를 리스트의 길이로 나눈 나머지로 업데이트하면 인덱스가 리스트의 범위를 벗어나지 않
    index = index % len(nums)
    ans.append(nums.pop(index))

print(f"<{', '.join(map(str, ans))}>")
