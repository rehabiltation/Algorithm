def function(N, budgets, M):
    start = 0
    end = max(budgets)
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for budget in budgets:
            if budget > mid:
                total += mid
            else:
                total += budget
        
        if total <= M:
            start = mid + 1
        else:
            end = mid - 1
    
    return end

# 입력 받기
N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

# 결과 출력
result = function(N, budgets, M)
print(result)
