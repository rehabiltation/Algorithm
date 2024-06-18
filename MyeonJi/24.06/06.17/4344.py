# 소요시간:
# 특이사항: `f{#}`오만거 다 쳐봄 기억이 안나서 ㅠ

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    c = 0
    for i in nums[1:]:
        avg = sum(nums[1:]) / nums[0]
        if i > avg:
            c += 1
    rate = c / nums[0] * 100
    print('{0:0.3f}%'.format(rate))
