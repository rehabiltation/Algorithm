def count_pairs(A, B):
    A.sort()
    B.sort()
    
    count = 0
    j = 0
    for a in A:
        while j < len(B) and B[j] < a:
            j += 1
        count += j
    return count

# 입력 처리
T = int(input())

results = []
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    results.append(count_pairs(A, B))

# 결과 출력
for result in results:
    print(result)
