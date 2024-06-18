# 소요시간: 9분
# 특이사항: print('{num} = {n + for n in nums}') 이지랄

while True:
    num = int(input())
    if num == -1:
        break
    else:
        nums = []
        for i in range(1, num):
            if num % i == 0:
                nums.append(i)
        if sum(nums) == num:
            print(f"{num} = {' + '.join(map(str, nums))}")
        else:
            print(f"{num} is NOT perfect.")
