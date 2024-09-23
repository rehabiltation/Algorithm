def n_queen(n):
    # 각 열에 퀸을 놓았는지 확인하는 배열
    cols = [False] * n
    # "/" 방향 대각선을 확인하는 배열
    diag1 = [False] * (2 * n - 1)
    # "\" 방향 대각선을 확인하는 배열
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # 퀸을 놓을 수 있으면 배치하고 백트래킹을 수행
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                count += backtrack(row + 1)
                # 다시 퀸을 놓은 자리를 초기화 (백트래킹)
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
        return count

    return backtrack(0)

# 입력 받기
n = int(input())

# 결과 출력
print(n_queen(n))
