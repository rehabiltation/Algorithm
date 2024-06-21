# 소요시간:
# 특이사항: 시간초과 ㅠ

N = int(input())
# nums 리스트를 set으로 변환하여 존재 여부 확인을 빠르게 처리
nums = set(map(int, input().split()))  
M = int(input())
num = list(map(int, input().split()))

for n in num:
    if n in nums:
        print(1)
    else:
        print(0)
