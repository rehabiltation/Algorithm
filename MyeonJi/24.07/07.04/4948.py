'''
# 에라토스테네스의 체 알고리즘
1. 초기화: 2부터 n까지의 모든 정수를 나열합니다.
2. 첫 소수 선택: 가장 작은 소수를 찾습니다. 처음에는 2가 됩니다.
3. 소수의 배수 제거: 현재 소수의 배수를 모두 제거합니다.
4. 반복: 다음 소수를 선택하고, 그 소수의 배수를 제거하는 과정을 반복합니다.
5. 종료: 선택한 소수가 루트n을 넘을 때까지 반복합니다. 남은 수는 모두 소수입니다.
'''

import sys
input = sys.stdin.read

def sieve_of_eratosthenes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False  # 0과 1은 소수가 아님
    p = 2
    while p * p <= limit:
        if nums[p]:
            for multiple in range(p * p, limit + 1, p):
                nums[multiple] = False
        p += 1
    return nums

def count_primes_in_range(nums, start, end):
    return sum(1 for i in range(start + 1, end + 1) if nums[i])

# 최대값 설정
MAX_N = 123456
MAX_LIMIT = 2 * MAX_N

# 에라토스테네스의 체로 소수 구하기
nums = sieve_of_eratosthenes(MAX_LIMIT)

# 입력 처리
data = input().strip().split()
num_list = list(map(int, data))

# 각 n에 대해 n보다 크고 2n 이하의 소수 개수 출력
for n in num_list:
    if n == 0:
        break
    print(count_primes_in_range(nums, n, 2 * n))


'''
num = 123456*2+1
num_list = [1]*num
for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    if n == 0:
        break
    prime = 0
    for i in range(n+1, 2*n+1):
        prime += num_list[i]
    print(prime)
    '''