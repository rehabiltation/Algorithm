# 소요시간:
# 특이사항: 부분수열구해서 걍 다 더해봄 난이도 올라가면 무조건 시간초과나겟지,,

N, S = map(int, input().split())
nums = list(map(int, input().split()))

def all_subsequences(arr):
    n = len(arr)
    subsequences = []
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(arr[j])
        subsequences.append(subsequence)
    return subsequences

all_list = all_subsequences(nums)
cnt = 0

for a in all_list:
    if a.length == 0:
        pass
    else:
        if sum(a) == S:
            cnt += 1

print(cnt)