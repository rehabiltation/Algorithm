# 소요시간:
# 특이사항:

N = int(input())
P = list(map(int, input().split()))
# 시간 오름차순 정렬
P.sort()

# 각 사람이 돈을 인출하는데 걸리는 시간의 합 계산
total_time = 0
current_sum = 0

for time in P:
    current_sum += time
    total_time += current_sum

# 결과 출력
print(total_time)
